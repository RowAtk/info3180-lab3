from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    """ fields for name, email, subject and a text area for a message. Also remember to protect your form with a CSRF token. """
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label="E-mail Address", validators=[
        DataRequired(message="This field is required"), 
        Email(message="Invalid email address")
        ])
    subject = StringField(label='Subject')
    message = TextAreaField(label="Message to be sent")