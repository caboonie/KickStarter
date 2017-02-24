from flask import Flask, render_template, request, flash, url_for, redirect
from model import * 
import random
from flask import session as login_session
from passlib.apps import custom_app_context as pwd_context
from flask_httpauth import HTTPBasicAuth
import sys
import logging


app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)




app.secret_key = '#$#UJEJOIBVJWOI'




def verify_password(username, password):
    user = session.query(User).filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    return True

@app.route("/")
@app.route("/main")
def showLandingPage():
	return render_template("landingPage.html")


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