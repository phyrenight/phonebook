from flask import Flask, render_template, request, session, redirect, url_for
from forms import SignUpForm, LoginForm, ContactForm
from database_setup import User, Contact, session as db_session

app = Flask(__name__)

app.secret_key = "development-key"

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/signup", methods=['GET', 'POST'])
def SignUp():
    if 'email' in session:
        return redirect(url_for('home'))

    form = SignUpForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('Signup.html', form=form)
        else:
            users = User( form.first_name.data, form.last_name.data, form.password.data, form.email.data)
            db_session.add(users)
            db_session.commit()
            session['email'] = form.email
            return redirect(url_for('home'))
    elif request.method == 'GET':
        return render_template('Signup.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def Login():
    if 'email' in session:
        return redirect(url_for('home'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('login.html', form=form)
        else:
            email = form.email.data
            password = form.password.data

            user = db_session.query(User).filter_by(email=email).first()
            if user is not None and (user.password == password):
                session['email'] = form.email.data
                return redirect(url_for('home'))
            else:
                return redirect(url_for('Login'))
    elif request.method == 'GET':
        return render_template('login.html', form=LoginForm())

@app.route("/newcontact", methods=['GET', 'POST'])
def NewContact():
    if 'email' not in session:
	    return redirect(url_for('Login'))
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('newcontact.html', form=form)
        else:
            contacts = Contact()
            if form.first_name.data:
                contacts.firstname = form.first_name.data
            if form.last_name.data:
                contacts.lastname = form.last_name.data
            if form.email.data:
                contacts.email = form.email.data
            if form.phonenumber:
                contacts.phoneNumber =  form.phone_number.data
            if form.address.data:
                contacts.address = form.address.data
            db_session.add(contacts)
            db_session.commit()
    elif request.method == 'GET':
        return render_template('newcontact.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)