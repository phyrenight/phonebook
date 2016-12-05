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
                print user
                return user
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
    pass

def edit_contact(contactName):
    pass

def delete_contact(contactName):
    pass

def get_users_contacts(user):
    pass

def find_contact_by_email(email):
    pass

def find_contact_by_address(address):
    pass

def find_contact_by_name(contact):
    pass

def find_contact_by_phoneNumber(phone):
    pass

delete_User(" ")
delete_User("  ")