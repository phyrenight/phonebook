from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database_setup import User, Contact, Base


engine = create_engine('sqlite:///Phonebook.db')
Base.metadata.bind = engine
DB = sessionmaker(bind=engine)
Base.metadata.create_all()
session = DB()


def register_user(login):
    if login['name'] != None:
        newUser = User(name = login['name'], email = login['email'])
        session.add(newUser)
        session.commit()
        user = session.query(User).filter_by(email=login['email']).one()
        return user.id
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
    if userName != None:
        try:
            user = session.query(User).filter_by(name = userName).one()
            session.delete(user)
            session.commit()
            return "user deleted"
        except:
            return "User not found."
    else:
        return None

def create_contact():
    pass

def edit_contact():
    pass

def delete_contact():
    pass

def get_users_contacts():
    pass

def find_contact_by_email():
    pass

def find_contact_by_address():
    pass

def find_contact_by_name():
    pass

def find_contact_by_phoneNumber():
    pass

