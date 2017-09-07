from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignUpForm(FlaskForm):
    first_name = StringField('First name',
                             validators=[DataRequired
                             ("Please enter your first name")])
    last_name = StringField('Last name', 
                            validators=
                                       [DataRequired("Please enter your last name")])
    email = StringField('Email',
                         validators=
                                     [DataRequired("Please enter your email address"), Email("Please enter a valid email address")])
    password = PasswordField('Password',
                              validators=[DataRequired
                              ("Please enter a password"),
                               Length(min=6, 
                               message="Password must be at least 6 characters long")])
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired
                        ("Please enter your email address"),
                         Email("Please enter a valid email")])
    password = PasswordField('Password',
                             validators=[DataRequired
                             ("Please enter your password")])
    submit = SubmitField('Sign in')

class ContactForm(FlaskForm):
   first_name = StringField('First name',
                             validators=[DataRequired
                             ("Please enter a first name for this contact")])
   last_name = StringField('Last name', validators=[DataRequired("Please enter a last name for this contact")])
   phone_number = StringField('Phone number',
                               validators=[DataRequired
                               ("Please enter a phone number"),
                                Length(min=6,
                                 message="Please enter a valid phone number")])
   email = StringField('Email')
   address = StringField('Address')
   submit = SubmitField('Submit contact')

class RequestPasswordReset(FlaskForm):
    email = StringField('email',
                         validators=[DataRequired
                         ("Please enter your email address.")])
    submit = SubmitField('Submit request')