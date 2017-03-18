# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, flash, url_for, redirect, send_from_directory, jsonify
from model import * 
import random
from flask import session as login_session
from passlib.apps import custom_app_context as pwd_context
from flask_httpauth import HTTPBasicAuth
import sys
import logging
from werkzeug.utils import secure_filename
import os
import datetime
from random import randint
from validate_email import validate_email
from flask_mail import Mail
from flask_mail import Message
from flask_oauthlib.client import OAuth, OAuthException 

import json 
import string
CONFIG = json.loads(open('secrets.json', 'r').read())

LAUNCHDATE = datetime.datetime.strptime('25/03/2017', "%d/%m/%Y").date()
DEADLINE = datetime.datetime.strptime('31/03/2017', "%d/%m/%Y").date()

with open('silvermembers.txt') as f:
    silverMembers = f.read().splitlines()
with open('goldmembers.txt') as f:
    goldMembers = f.read().splitlines()


app = Flask(__name__)
app.config['GOOGLE_ID'] = CONFIG['GOOGLE_ID']
app.config['GOOGLE_SECRET'] = CONFIG['GOOGLE_SECRET']
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
app.secret_key = CONFIG['SECRET_KEY']
oauth = OAuth(app)


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# email server
app.config.update(
MAIL_SERVER=CONFIG['MAIL_SERVER'],
MAIL_PORT = CONFIG['MAIL_PORT'],
MAIL_USERNAME = CONFIG['MAIL_USERNAME'],
MAIL_PASSWORD= CONFIG['MAIL_PASSWORD'],
MAIL_USE_TLS = False,
MAIL_USE_SSL = True)

google = oauth.remote_app(
    'google',
    consumer_key=app.config.get('GOOGLE_ID'),
    consumer_secret=app.config.get('GOOGLE_SECRET'),
    request_token_params={
        'scope': 'https://www.googleapis.com/auth/userinfo.email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)
# administrator list
ADMINS = [CONFIG['MAIL_USERNAME']]

mail = Mail(app)

##FACEBOOK CONFIGURATIONS## 
FACEBOOK_APP_ID = CONFIG['FACEBOOK_APP_ID']
FACEBOOK_APP_SECRET = CONFIG['FACEBOOK_APP_SECRET']


oauth = OAuth()

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'email'}
)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def verify_password(email, password):
    user = session.query(User).filter_by(email=email).first()
    if not user or not user.verify_password(password):
        return False
    return True

@app.route('/loginWithGoogle')
def loginWithGoogle():
	#callback = 'https://meetcampaign.herokuapp.com/loginWithGoogle/authorized'
	#return google.authorize(callback=callback)
    return google.authorize(callback=url_for('authorized', _external=True))
@app.route('/loginWithGoogle/authorized')
def authorized():
	resp = google.authorized_response()
	if resp is None:
		return 'Access denied: reason=%s error=%s' % (
		request.args['error_reason'],
		request.args['error_description']
		)
	login_session['google_token'] = (resp['access_token'], '')
	me = google.get('userinfo')
	first_name = me.data['given_name']
	last_name = me.data['family_name']
	email = me.data['email']
	query = session.query(User).filter_by(email=email).one_or_none()
	if query == None:
		newUser = User(first_name = first_name, last_name = last_name, email = email, verified=True)
		if email in goldMembers:
			newUser.group = "gold"
		elif email in silverMembers:
			newUser.group = "silver"
		else:
			newUser.group = "bronze"
		session.add(newUser)
		session.commit()
		## Make a Wallet for  newUser
		if email in goldMembers:
			usersWallet = Wallet(initial_value = '1000000.00', current_value = '1000000.00', user = newUser)
		elif email in silverMembers:
			usersWallet = Wallet(initial_value = '100000.00', current_value = '100000.00', user = newUser)
		else:
			usersWallet = Wallet(initial_value = '10000.00', current_value = '10000.00', user = newUser)
		session.add_all([newUser,usersWallet])
		session.commit()
	else:
		newUser = query

	login_session.clear()
	login_session['first_name'] = newUser.first_name
	login_session['id'] = newUser.id
	login_session['last_name'] = newUser.last_name
	login_session['group'] = newUser.group
	flash("Login Successful. Welcome, %s!" % newUser.first_name)
	return redirect(url_for('showProducts'))


@google.tokengetter
def get_google_oauth_token():
    return login_session.get('google_token')

@app.route("/")
@app.route("/main")
def showLandingPage():
	now = datetime.datetime.now().date()
	if now < LAUNCHDATE:
		return render_template("prelaunchlanding.html")
	return render_template("landingPage.html")

@app.route('/loginWithFacebook')
def loginWithFacebook():
	#callback = url_for('facebook_authorized', next = request.args.get('next') or request.referrer or None, _external=True)
	callback = 'https://meetcampaign.herokuapp.com/loginWithFacebook/authorized'
	return facebook.authorize(callback=callback)

# return facebook.authorize(callback=url_for('facebook_authorized',
#    next=request.args.get('next') or request.referrer or None,
#   _external=True))


@app.route('/loginWithFacebook/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
	if resp is None:
		return 'Access denied: reason=%s error=%s' % (
		request.args['error_reason'],
		request.args['error_description']
		)
	if isinstance(resp, OAuthException):
		return 'Access denied: %s' % resp.message
	login_session['oauth_token'] = (resp['access_token'], '')
	me = facebook.get('/me?fields=name,email')
	name = me.data['name']
	email = me.data['email']
	query = session.query(User).filter_by(email=email).one_or_none()
	if query == None:
		newUser = User(first_name = name.split(" ")[0], last_name = name.split(" ")[1], email = email, verified=True)
		if email in goldMembers:
			newUser.group = "gold"
		elif email in silverMembers:
			newUser.group = "silver"
		else:
			newUser.group = "bronze"
		session.add(newUser)
		session.commit()
		## Make a Wallet for  newUser
		if email in goldMembers:
			usersWallet = Wallet(initial_value = '1000000.00', current_value = '1000000.00', user = newUser)
		elif email in silverMembers:
			usersWallet = Wallet(initial_value = '100000.00', current_value = '100000.00', user = newUser)
		else:
			usersWallet = Wallet(initial_value = '10000.00', current_value = '10000.00', user = newUser)
		session.add_all([newUser,usersWallet])
		session.commit()
	else:
		newUser = query

	login_session.clear()
	login_session['first_name'] = newUser.first_name
	login_session['id'] = newUser.id
	login_session['last_name'] = newUser.last_name
	login_session['group'] = newUser.group
	flash("Login Successful. Welcome, %s!" % newUser.first_name)
	return redirect(url_for('showProducts'))
    

@facebook.tokengetter
def get_facebook_oauth_token():
    return login_session.get('oauth_token')

@app.route("/signup", methods = ['GET', 'POST'])
def signup():
	if request.method == 'GET':
		return render_template('signup.html')
	elif request.method == 'POST':
		first_name = request.form['first_name']
		last_name = request.form['last_name']
		hometown = request.form['hometown']
		email = request.form['email']
		password = request.form['password']
		verify_password = request.form['verify_password']
		if password != verify_password:
			flash("Passwords do not match")
			return redirect(url_for('signup'))
		if session.query(User).filter_by(email=email).all() != []:
			flash("A User already exists with this email address")
			return redirect(url_for('signup'))
		if validate_email(email, verify=True)!=False:
			newUser = User(first_name=first_name, last_name=last_name, hometown = hometown,email=email, verified=False)
			if email in goldMembers:
				newUser.group = "gold"
			elif email in silverMembers:
				newUser.group = "silver"
			else:
				newUser.group = "bronze"
			session.add(newUser)
			session.commit()
			newUser.confirmation_code = generateConfCode()
			newUser.confirmation_code_expiration = datetime.datetime.now() + datetime.timedelta(minutes = 10)
			newUser.hash_password(password)
			session.add(newUser)
			session.commit()
			send_email("Verify your MEETCampaign Account",ADMINS[0],[newUser.email],render_template("confirmationemail.txt", user=newUser),
	           render_template("confirmationemail.html", user=newUser))
			flash("Please check your email to verify your confirmation code")
			return redirect(url_for('verify', email = email))
		else:
			flash("This email is invalid. Please try again")
			return redirect(url_for('signup'))

		

@app.route("/verify/<email>", methods = ['GET', 'POST'])
def verify(email):
	user = session.query(User).filter_by(email=email).one()
	if user.confirmation_code_expiration < datetime.datetime.now():
		flash("This confirmation code has expired. Please request a new code.")
		return redirect(url_for('resendCode', email = user.email))
	if request.method == 'GET':
		return render_template('verifyAccount.html', user=user)
	elif request.method == 'POST':
		code = request.form['code']
		if user.confirmation_code == code:
			user.verified = True
		else:
			flash("Verification code incorrect. Please try again")
			return redirect(url_for('verify', email = email))
		## Make a Wallet for verified user
		## Make a Wallet for  newUser
		if email in goldMembers:
			usersWallet = Wallet(initial_value = '1000000.00', current_value = '1000000.00', user = user)
		elif email in silverMembers:
			usersWallet = Wallet(initial_value = '100000.00', current_value = '100000.00', user = user)
		else:
			usersWallet = Wallet(initial_value = '10000.00', current_value = '10000.00', user = user)
		session.add_all([user,usersWallet])
		session.commit()
		flash("Account Verfied Successfully")
		return redirect(url_for('login'))

@app.route("/resendCode/<email>", methods = ['GET', 'POST'])
def resendCode(email):
	user = session.query(User).filter_by(email=email).one()
	if request.method == 'GET':
		return render_template('resendCode.html', email=email)
	if request.method == 'POST':
		user.confirmation_code = generateConfCode()
		user.confirmation_code_expiration = datetime.datetime.now() + datetime.timedelta(minutes = 10)
		session.add(user)
		session.commit()
		send_email("Resetting your MEETCampaign Account Code",ADMINS[0],[user.email],render_template("confirmationemail.txt", user=user),
               render_template("confirmationemail.html", user=user))
		flash("A new verification code has been sent to your email address")
		return redirect(url_for('verify', email = email))

@app.route("/forgotPassword", methods = ['GET', 'POST'])
def forgotPassword():
	if request.method == 'GET':
		return render_template('passwordReset.html')
	elif request.method == 'POST':
		email = request.form['email']
		user = session.query(User).filter_by(email=email).one_or_none()
		if user == None:
			flash("No user exists with this email address.  Please create a new account")
			return redirect(url_for('signup'))
		else:
			user.confirmation_code = generateConfCode()
			user.confirmation_code_expiration = datetime.datetime.now() + datetime.timedelta(minutes = 10)
			session.add(user)
			session.commit()
			send_email("Resetting your MEETCampaign Password",ADMINS[0],[user.email],render_template("resetpassword.txt", user=user),
               render_template("resetpassword.html", user=user))
			flash("A new confirmation code has been sent to your email")
			return redirect(url_for('resetPassword', email=email))

@app.route("/resetPassword/<email>", methods = ['GET','POST'])
def resetPassword(email):
	user = session.query(User).filter_by(email=email).one_or_none()
	if request.method == 'GET':
		return render_template('resetpasswordverificationcode.html', user = user)
	elif request.method == 'POST':
		code = request.form['code']
		password = request.form['password']
		verify_password = request.form['verify_password']
		if user.confirmation_code_expiration < datetime.datetime.now():
			flash("This confirmation code has expired. Please request a new code.")
			return redirect(url_for('passwordReset', email = user.email))
		if user.confirmation_code == code:
			if password == verify_password:
				user.hash_password(verify_password)
				session.add(user)
				session.commit()
				flash("Account Verfied Successfully")
				return redirect(url_for('login'))
			else:
				flash("Passwords do not match")
				return redirect(url_for('resetPassword', email = email))
		else:
				flash("Incorrect verifcation code")
				return redirect(url_for('resetPassword', email = email))

@app.route("/language/<language>")
def changeLanguage(language):
	login_session['language'] = language
	return redirect(request.referrer)

@app.route('/notify', methods = ['POST'])
def notifyList():
	email = request.form['email']
	newEmail = MailingList(email=email)
	session.add(newEmail)
	session.commit()
	if login_session['language'] == 'ar':
		flash("شكرا جزيلا ! سوف يتم إعلامك عندما تبدأ الحملة")
	elif login_session['language'] == 'he':
		flash("תודה רבה! ניצור אתכם קשר כשהקמפיין יתחיל.")
	else:
		flash("Thank You! You will be notified when the campaign begins")
	return redirect(url_for('showLandingPage'))

@app.route("/login", methods = ['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		email = request.form['email']
		password = request.form['password']
		if email is None or password is None:
			flash("Missing Arguments")
			return redirect(url_for('login'))
		if verify_password(email, password):
			user = session.query(User).filter_by(email=email).one()
			if user.verified == False:
				flash("You must verify your account before continuing")
				return redirect(url_for('verify', email = email))
			flash("Login Successful. Welcome, %s!" % user.first_name)
			login_session['first_name'] = user.first_name
			login_session['last_name'] = user.last_name	
			login_session['email'] = email
			login_session['id'] = user.id
			login_session['group'] = user.group
			if user.group == 'student':
				return redirect(url_for('studentPortal'))
			if user.group == 'administrator':
				return redirect(url_for('adminPortal'))
			return redirect(url_for('showProducts'))
		else:
			flash("Incorrect email/password combination")
			return redirect(url_for('login'))
@app.route('/logout')
def logout():
	if 'id' not in login_session:
		flash("You must be logged in in order to log out")
		return redirect(request.referrer)
	login_session.clear()
	flash ("Logged Out Successfully")
	return redirect(url_for('showLandingPage'))


@app.route("/studentPortal")
def studentPortal():
	if login_session['group'] != 'student':
		flash("This page is only accessible to students")
		return redirect(url_for('login'))
	user = session.query(User).filter_by(id = login_session['id']).one()
	team = session.query(Team).filter_by(id=user.team_id).one()
	product = session.query(Product).filter_by(team_id = team.id).one()
	comments = session.query(Comment).filter_by(product_id =product.id).all()
	total_investments = 0.0
	for inv in product.investments:
		total_investments += inv.amount
	return render_template('teamPortal.html', user=user, team=team, comments = comments, total_investments = total_investments)


@app.route("/updateSubmission", methods = ['POST'])
def updateSubmission():
	team_name = request.form['team_name']
	description_en = request.form['description_en']
	description_ar = request.form['description_ar']
	description_he = request.form['description_he']
	website_url = request.form['website_url']
	video_url = request.form['video_url']
	photo_url = request.form['photo_url']
	user = session.query(User).filter_by(id = login_session['id']).one()
	team = session.query(Team).filter_by(id=user.team_id).one()
	team.name = team_name
	team.product.description_en = description_en
	team.product.description_ar = description_ar
	team.product.description_he = description_he
	team.product.website_url = website_url
	team.product.video_url = video_url
	team.product.photo = photo_url
	flash("Team Info Updated Successfully!")
	session.add(team)
	session.commit()
	return redirect(url_for('studentPortal'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/addComment/<int:team_id>', methods = ['POST'])
def addComment(team_id):
	product = session.query(Product).filter_by(team_id=team_id).one()
	comment = Comment(text = request.form['commentary'], product=product)
	session.add(comment)
	session.commit()
	flash("Thank you for your feedback!")
	return redirect(request.referrer)

@app.route("/adminPortal")
def adminPortal():
	if login_session['group'] != 'administrator':
		flash("This page is only accessible by administrators")
		return redirect(url_for('login'))
	users = session.query(User).all()
	teams = session.query(Team).all()
	investments = session.query(Investment).all()
	return render_template('teamPortal.html', user=user, team=team)

@app.route("/products")
def showProducts():
	if 'id' not in login_session:
		flash("You must be logged in to view this page.")
		return redirect(url_for('login'))
	products = session.query(Product).all()
	wallet = session.query(Wallet).filter_by(user_id = login_session['id']).one_or_none()
	return render_template('productsPage.html', products = products, wallet = wallet)

@app.route("/product/<int:product_id>")
def showProduct(product_id):
	product = session.query(Product).filter_by(id = product_id).one()
	wallet = session.query(Wallet).filter_by(user_id = login_session['id']).one_or_none()
	return render_template('productPage.html', product = product, wallet = wallet)

@app.route("/makeAnInvestment/<int:product_id>", methods = ['POST'])
def makeAnInvestment(product_id):
	amount = float(request.form['amount'])
	wallet = session.query(Wallet).filter_by(user_id =login_session['id']).one_or_none()
	product = session.query(Product).filter_by(id = product_id).one()
	if wallet.current_value > amount:
		inv = Investment(wallet_id = wallet.id, product_id = product.id, amount = amount)
		wallet.current_value = wallet.current_value - amount
		session.add_all([wallet,inv])
		session.commit()
		flash("Successfully invested %s for %s. Thank you for your investment!" % (str(amount), product.team.name))
		return redirect(url_for('showProducts'))
	else:
		flash("You not have enough money to make this investment")
		return redirect(url_for('showProduct', product_id = product_id))
@app.route("/showDashboard")
def showDashboard():
	products = session.query(Product).all()
	bronze_investors = session.query(User).filter_by(group = 'bronze').all()
	silver_investors = session.query(User).filter_by(group = 'silver').all()
	gold_investors = session.query(User).filter_by(group = 'gold').all()
	totals = []
	for product in products:
		total_investments = 0.0
		for inv in product.investments:
			total_investments += inv.amount
		totals.append(total_investments)
	return render_template('dashboard.html', totals = totals, products = products, bronze_investors = bronze_investors, silver_investors = silver_investors, gold_investors = gold_investors)

def generateConfCode():
	return str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    with app.app_context():
    	mail.send(msg)
if __name__ == '__main__':
	app.run(debug=True)