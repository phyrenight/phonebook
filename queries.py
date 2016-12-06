from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database_setup import User, Contact, Base


engine = create_engine('sqlite:///Phonebook.db')
Base.metadata.bind = engine
DB = sessionmaker(bind=engine)
Base.metadata.create_all()
session = DB()

# rewrite functions to work with string or a dict

def register_user(login):
    if type(login) == dict:
        if login['name'] != None and login['name'] != "":
            try:
                checkUsername = session.query(User).filter_by(name = login['name']).one()
            except:
                newUser = User(name = login['name'], email = login['email'])
                session.add(newUser)
                session.commit()
                user = session.query(User).filter_by(name=login['name']).one()
                return "User registered"
            else:
                return "Username already in use."
        else:
            return None
    else:
        return None

def get_user(name):
    try:
     	user = session.query(User).filter_by(name = name).one()
    except Exception, e:
        user = None
    #   raise 
    #else:
    # 	pass
    #finally:
    # 	pass
    return user

def get_user_by_email(email):
    user = session.query(User).filter_by(email = email).one()
    if user == None:
        return None
    else:
        return user

def delete_User(userName):
    if userName:
        try:
            user = session.query(User).filter_by(name = userName).one()
            session.delete(user)
            session.commit()
            return "user deleted"
        except:
            return "User not found."
    else:
        return None

def create_contact(contact):
    if contact != None:
        if contact['name']:
            try:
                testContact = session.query(Contact).filter_by(name = contact['name']).one()
            except:
                newContact = Contact(name = contact['name'])
                if contact['phone'] != "":
                    newContact.phone = contact['phone']
                if contact['email'] != "":
                    newContact.email = contact['email']
                if contact['address'] != "":
                    newContact.address = contact['address']
                session.add(newContact)
                session.commit()
                return "Contact created."
            else:
                return "Contact already exist."
        else:
            return "Invalid input"

def edit_contact(contactName):
    if contactName != None and contactName !="":
        try:
            contact = session.query(Contact).filter_by(name = contactName['name']).one()
        except:
            return "No contact by that name"
        else:
            if contactName['name'] != None or "":
                contact.name = contactName['name']
            if contactName['phone'] != None or "":
                contact.phone = contactName['phone']
            if contactName['email'] != None or "":
                contact.address = contactName['address']
            session.add(contact)
            session.commit()
            return "Contact has been edited."
    else:
        return "Invalid input"

def delete_contact(contactName):
    if contactName != None:
        try:
            contact = session.query(Contact).filter_by(name = contactName).one()
            session.delete(contact)
            session.commit()
            return "Contact deleted"
        except:
            return "No contact by the name {}".format(contactName)
    else:
        return "Invalid input"

def get_users_contacts(user):
    pass

def find_contact_by_email(emailAddress):
    if emailAddress:
        try:
            email = session.query(Contact).filter_by(email = emailAddress).one()
        except:
            return "No contact with that email."
        else:
            return email
    else:
        return "Invalid input"

def find_contact_by_address(address):
    pass

def find_contact_by_name(contact):
    pass

def find_contact_by_phoneNumber(phone):
    pass

