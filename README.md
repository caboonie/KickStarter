# KickStarter
Voting Website for Y2 Yearlong Group Projects

## Running Locally:

### Required Packages
All of the packages for this website can be installed using the pip installer.
It's generally good practice to work within a virtual environment which can be created and then activated with the following:
```
virtualenv -p python3 venv
source venv/bin/activate
```
Then, the dependencies can easily be installed by running:
```
pip install -r requirements.txt
```

<ul>
<li>pandas(for database populating)</li>
<li>flask</li>
<li>Flask-HTTPAuth</li>
<li>Jinja2</li>
<li>passlib</li>
<li>python-dateutil</li>
<li>requests</li>
<li>SQLAlchemy</li>
<li>psycopg2</li>
<li>validate_email</li>
<li>flask_mail</li>
<li>flask_oauthlib</li>
<li>Py3DNS</li>
<!-- <li>pyDNS</li>  -->
</ul>


1.  Fill in the values of secrets.json with your own credentials.
	- The Google and Facebook IDs/secrets are for enabling oauth2 log-in using Google and Facebook.
	- The MAIL_USERNAME/PASSWORD are for the email account to send emails out from. A meet email was created to send the automatic emails: noreply.meet.mit@gmail.com . Ask the staff for the password.

2. Run python intializeDB.py

3. In webapp.py, comment out lines 24 and 25 if you are using Python 3.

4. In webapp.py, toggle the comments on line 181 and line 182

5. Run python webapp.py 

hopefully it should run on localhost:5000 without any problems.

Important files:  all html in templates folder all templates inherit from layout.html , all css files in static folder,

Ping me if you run into any problems.