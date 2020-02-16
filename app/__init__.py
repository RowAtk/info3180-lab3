import os
from flask import Flask 
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__) 
app.config['SECRET_KEY'] = os.urandom(24) 
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io' 
app.config['MAIL_PORT'] = '2525' # (or try 46) 
app.config['MAIL_USERNAME'] = '' 
app.config['MAIL_PASSWORD'] = '' 
mail = Mail(app)
csrf = CSRFProtect(app)

from app import views