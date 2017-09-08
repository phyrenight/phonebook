from flask import Flask, render_template, request, session, redirect, url_for
from flask import flash
from forms import SignUpForm, LoginForm, ContactForm, RequestPasswordReset
from database_setup import User, Contact, session as db_session
from flask.ext.bcrypt import Bcrypt
from flask_mail import Mail, Message
from config import mail_server, mail_port, mail_username, mail_password
app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['MAIL_SERVER'] = mail_server
app.config['MAIL_PORT'] = mail_port
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

app.secret_key = "development-key"

mail = Mail(app)

@app.route("/")
@app.route("/home")
def home():
    msg = Message('Hello', sender=mail_username, recipients = ['preston9@comcast.net'])
    msg.body = "hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return render_template('home.html')

@app.route("/signup", methods=['GET', 'POST'])
def SignUp():
    if 'email' in session:
        return redirect(url_for('Contacts'))

    form = SignUpForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash("please fill out the form completely")
            return render_template('Signup.html', form=form)
        else:
            if db_session.query(User).filter_by(email=form.email.data).first():
                flash("Email already in use")
                return render_template('Signup.html', form=form)
            else:
                pw_hash = bcrypt.generate_password_hash(form.password.data)
                users = User( form.first_name.data, form.last_name.data, pw_hash, form.email.data)
                db_session.add(users)
                db_session.commit()
                session['email'] = form.email.data
                return redirect(url_for('Contacts'))
    elif request.method == 'GET':
        return render_template('Signup.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def Login():
    if 'email' in session:
        return redirect(url_for('Contacts'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('login.html', form=form)
        else:
            email = form.email.data
            password = form.password.data

            user = db_session.query(User).filter_by(email=email).first()
            if user is not None and bcrypt.check_password_hash(user.password, password):
                session['email'] = form.email.data
                return redirect(url_for('Contacts'))
            else:
                return redirect(url_for('Login'))
    elif request.method == 'GET':
        return render_template('login.html', form=form)

@app.route("/resetpassword", methods=['GET', 'POST'])
def resetPassword():
    if 'email' in session:
        return redirect(url_for('home'))
    form = RequestPasswordReset()
    
    if request.method == 'POST':
        print form.email.data
        if form.validate() == False:
            flash("Please enter a valid email.")
            return render_template('resetpassword.html', form=form)
        else:
            user = db_session.query(User).filter_by(email=form.email.data).first()
            if user is not None:
                return redirect(url_for('EmailSent'))
            else:
                flash("Email not in database")
                return redirect(url_for('resetPassword'))
    elif request.method == 'GET':
        return render_template('resetpassword.html', form=form)

@app.route("/emailsent")
def EmailSent():
    return render_template('emailsent.html')

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

@app.route('/deletecontact/<contact>', methods=['GET', 'POST'])
def DeleteContact(contact):
    if 'email' not in session:
        return redirect(url_for('Login'))
    form = ContactForm()
    contactDetails = db_session.query(Contact).filter_by(contactId=contact).first()
    if request.method == 'GET':
        return render_template('deletecontact.html', contact=contactDetails)
    if request.method == 'POST':
        useremail = db_session.query(User).filter_by(id=contactDetails.UserId).first()
        if useremail.email == session['email']:
            contactDetails = db_session.query(Contact).filter_by(contactId=contact).first()
            db_session.delete(contactDetails)
            db_session.commit()
            flash("Contact has been deleted.")
            return redirect(url_for('Contacts'))
        else:
            flash("You are not the owner of this contact")
            return redirect(url_for('Login'))

@app.route('/editcontact/<contact>', methods=['GET', 'POST'])
def EditContact(contact):
    if 'email' not in session:
        return redirect(url_for('Login'))
    form = ContactForm()
    contactDetail = db_session.query(Contact).filter_by(contactId=contact).first()
    if request.method == 'POST':
        useremail = db_session.query(User).filter_by(id=contactDetail.UserId).first()
        if useremail.email == session['email']:
            if form.email.data != contactDetail.email:
                contactDetail.email = form.email.data
            if form.address.data != contactDetail.address:
                contactDetail.address = form.email.data 
            if form.phone_number.data != contactDetail.phoneNumber:
                contactDetail.phoneNumber = form.phone_number.data
            db_session.commit()
            flash("Contact has been updated.")
            return redirect(url_for('Contacts'))
        else:
            flash("This is not your account")
            return redirect(url_for('Contacts'))

    elif request.method == 'GET':
        form.first_name.content = contactDetail.name
        form.last_name.content = contactDetail.name
        form.phone_number.content = contactDetail.phoneNumber
        form.email.content = contactDetail.email
        form.address.content = contactDetail.address
        return render_template('editcontact.html', contact=contactDetail, form=form)

@app.route('/logout')
def Logout():
    if 'email' in session:
        session.clear()
        flash("You have been logged out.")
        return redirect(url_for('home'))
    else:
        flash("You are not logged in.")
        return render_template('home.html')

@app.errorhandler(500)
def internal_error(error):
    return render_template("internalerror.html")

@app.errorhandler(404)
def file_not_found(error):
    return render_template('error404.html')

if __name__ == "__main__":
    app.run(debug=True)