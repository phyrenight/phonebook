from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database_setup import User, Contact, Base


engine = create_engine('sqlite:///Phonebook.db')
Base.metadata.bind = engine
DB = sessionmaker(bind=engine)
Base.metadata.create_all()
session = DB()


def createUser(Login):
	newUser = User(name = login)
def get_user(name):
    try:
     	user = session.query(User).filter_by(name = name).one()
    except Exception, e:
        user = None
    #   raise 
    #else:
    # 	pass
    #finally:
    # 	pass session.query(User).filter_by(name = name).one():
    #    user = session.query(User).filter_by(name = name).one()
    #    print user
    #    return  user
    return user

def get_User_By_Email(email):
    user = session.query(User).filter_by(email = email).one()
    if user == None:
        return None
    else:
        return user
