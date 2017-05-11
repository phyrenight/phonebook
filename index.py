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
            session['email'] = form.email.data
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
            email = session['email']
            user = db_session.query(User).filter_by(email=email).first()
            contacts = Contact()
            contacts.UserId = user.id
            if form.first_name.data and form.last_name.data:
                contacts.name = form.first_name.data + " " + form.last_name.data
            if form.email.data:
                contacts.email = form.email.data
            if form.phone_number:
                contacts.phoneNumber =  form.phone_number.data
            if form.address.data:
                contacts.address = form.address.data
            db_session.add(contacts)
            db_session.commit()
            return redirect(url_for('Contacts'))
    elif request.method == 'GET':
        return render_template('newcontact.html', form=form)

@app.route("/contacts")
def Contacts():
    if 'email' not in session:
    	return redirect(url_for('Login'))
    else:
        mail =  str(session['email'])
    	user = db_session.query(User).filter_by(email=mail).first()
    	contacts = db_session.query(Contact).filter_by(UserId=user.id)
    	return render_template('contacts.html', contacts=contacts)

@app.route('/contact/<contact>')
def ContactDetails(contact):
    if 'email' not in session:
        return redirect(url_for('Login'))
    else:
        contactDetails = db_session.query(Contact).filter_by(contactId=contact).first()
        return render_template('contactInfo.html', contact=contactDetails)

@app.route('/deletecontact/<contact>')
def DeleteContact(contact):
    if 'email' not in session:
        return redirect(url_for('Login'))

    elif request.method == 'GET':
        contactDetails = db_session.query(Contact).filter_by(contactId=contact).first()
        return render_template('deletecontact.html',contact=contactDetails)

@app.route('/editcontact/<contact>')
def EditContact(contact):
    if 'email' not in session:
        return redirect(url_for('Login'))
    form = ContactForm()
    if request.method == 'GET':
        contactDetail = db_session.query(Contact).filter_by(contactId=contact).first()
        print contactDetail.name
        return render_template('editcontact.html', contact=contactDetail, form=form)
    elif request.method == 'POST':
        return redirect(url_for('Contacts'))

if __name__ == "__main__":
    app.run(debug=True)