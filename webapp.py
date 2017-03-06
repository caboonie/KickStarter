from flask import Flask, render_template, request, flash, url_for, redirect, send_from_directory
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


LAUNCHDATE = datetime.datetime.strptime('25/03/2017', "%d/%m/%Y").date()
DEADLINE = datetime.datetime.strptime('31/03/2017', "%d/%m/%Y").date()


app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)




app.secret_key = '#$#UJEJOIBVJWOI'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def verify_password(username, password):
    user = session.query(User).filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    return True

@app.route("/")
@app.route("/main")
def showLandingPage():
	now = datetime.datetime.now().date()
	if now < LAUNCHDATE:
		return render_template("prelaunchlanding.html")
	return render_template("landingPage.html")
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
	flash("Thank You! You will be notified when the campaign begins")
	return redirect(url_for('showLandingPage'))

@app.route("/login", methods = ['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username = request.form['username']
		password = request.form['password']
		if username is None or password is None:
			flash("Missing Arguments")
			return redirect(url_for('login'))
		if verify_password(username, password):
			user = session.query(User).filter_by(username=username).one()
			flash("Login Successful. Welcome, %s!" % user.first_name)
			login_session['first_name'] = user.first_name
			login_session['last_name'] = user.last_name	
			login_session['username'] = username
			login_session['id'] = user.id
			login_session['group'] = user.group
			if user.group == 'student':
				return redirect(url_for('studentPortal'))
			if user.group == 'administrator':
				return redirect(url_for('adminPortal'))
			return redirect(url_for('showProducts'))
		else:
			flash("Incorrect username/password combination")
			return redirect(url_for('login'))
@app.route('/logout')
def logout():
	if 'id' not in login_session:
		flash("You must be logged in in order to log out")
		return redirect(url_for('mainPage'))
	login_session.clear()
	flash ("Logged Out Successfully")
	return redirect(url_for('showLandingPage'))


@app.route("/studentPortal")
def studentPortal():
	if login_session['group'] != 'student':
		flash("This page is only accessible by students")
		return redirect(url_for('login'))
	user = session.query(User).filter_by(id = login_session['id']).one()
	team = session.query(Team).filter_by(id=user.team_id).one()
	return render_template('teamPortal.html', user=user, team=team)


@app.route("/updateSubmission", methods = ['POST'])
def updateSubmission():
	team_name = request.form['team_name']
	description_en = request.form['description_en']
	description_ar = request.form['description_ar']
	description_he = request.form['description_he']
	website_url = request.form['website_url']
	video_url = request.form['video_url']
	file = request.files['file']
	user = session.query(User).filter_by(id = login_session['id']).one()
	team = session.query(Team).filter_by(id=user.team_id).one()
	team.name = team_name
	team.product.description_en = description_en
	team.product.description_ar = description_ar
	team.product.description_he = description_he
	team.product.website_url = website_url
	team.product.video_url = video_url
	if file.filename != '':
		if file and allowed_file(file.filename):
			filename = str(team.id) + "_" + secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			team.product.set_photo(filename)
		else:
			flash("Please upload either a .jpg, .jpeg, .png, or .gif file.")
			return redirect(url_for('studentPortal'))
	flash("Team Info Updated Successfully!")
	session.add(team)
	session.commit()
	return redirect(url_for('studentPortal'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


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
	totals = []
	for product in products:
		total_investments = 0.0
		for inv in product.investments:
			total_investments += inv.amount
		totals.append(total_investments)
	return render_template('dashboard.html', totals = totals, products = products)
if __name__ == '__main__':
	app.run(debug=True)