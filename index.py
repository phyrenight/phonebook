from flask import Flask, render_template, request, session, redirect, url_for
from forms import SignUpForm, LoginForm, ContactForm
from database_setup import User, Contact

app = Flask(__name__)

app.secret_key = "development-key"

@app.route("/home")
def home():
   return render_template('home.html')


@app.route("/signup")
def SignUp():
	return render_template('Signup.html', form=SignUpForm())

@app.route("/login")
def Login():
	return render_template('login.html', form=LoginForm())

if __name__ == "__main__":
   app.run(debug=True)