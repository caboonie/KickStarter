## testing

from flask import Flask, render_template, request, flash, url_for, redirect, send_from_directory, jsonify, current_app
from flask_mail import Mail
from flask_mail import Message
import json
from model import * 

CONFIG = json.loads(open('secrets.json', 'r').read())

app = Flask(__name__)

app.config.update(
MAIL_SERVER=CONFIG['MAIL_SERVER'],
MAIL_PORT = CONFIG['MAIL_PORT'],
MAIL_USERNAME = CONFIG['MAIL_USERNAME'],
MAIL_PASSWORD= CONFIG['MAIL_PASSWORD'],
MAIL_USE_TLS = False,
MAIL_USE_SSL = True)

mail = Mail(app)

ADMINS = [CONFIG['MAIL_USERNAME']]

@app.route('/')
def home():
	subject = "Verify your MEETCampaign Account"
	sender = ADMINS[0]
	text_body = "Hi!"
	html_body = "<p>Hi!</p>"
	newUser = User(first_name="asl", last_name="asl", hometown = "asl",email="nayoung@mit.edu", verified=False)
	recipients = [newUser.email]
	msg = Message(subject, sender=sender, recipients=recipients)
	msg.body = render_template("confirmationemail_he.txt", user=newUser)
	msg.html = render_template("confirmationemail_he.html", user=newUser)
	with app.app_context():
		mail.send(msg)

	return "<p>Hello!</p>"

@app.route("/verify/<email>", methods = ['GET', 'POST'])
def verify(email):
	return "<p>verified</p>"
