from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators

# create a Python registration from class
# the python registration form class will then be converted to HTML form 
# all the form fields are imported classes as well
# RegistrationForm class will inherate from FlaskForm

class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=2, max=20)])
    email = StringField('Email', [validators.DataRequired(), validators.Email('Enter a valid Email')])
    password = PasswordField('Password', [validators.DataRequired()])
    confirm_password = PasswordField('Confirm Password', [validators.DataRequired(), validators.EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])
    remember = BooleanField('Remember Me') #uses a secure cookie to allow users to stay logged in after their browser closes 
    submit = SubmitField('Login')
