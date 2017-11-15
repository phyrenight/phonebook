from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, ForeignKeyConstraint

Base = declarative_base()

class User(Base):
    """Contains User information.

       :param int id: Unique id for the user
       :param str firstname: user's first name
       :param str lastname: user's last name
       :param str password: user's password
       :param str email: user's valid email
    
    """
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    password = Column(String(20),nullable=False)
    email = Column(String(250), nullable=False)  # should be unique

    def __init__(self, first_name, last_name, password, email):
        print first_name
        self.firstname = first_name
        self.lastname = last_name
        self.password = password
        self.email = email


class Contact(Base):
    """Contains info on each contact.

       :param int contactId: unique id for the contact
       :param int userId: unique key that is taken from the User table
       :param str name: name of the contact
       :param str phoneNumber: contact's phone number
       :param str address: contact's physical address
       :param str email: contact's valid email address 
    
    """
    __tablename__ = 'Contact'
    contactId = Column(Integer, primary_key=True)
    UserId = Column(Integer, ForeignKey('user.id')) #
    name = Column(String)
    phoneNumber = Column(String(20))
    address = Column(String(250))
    email = Column(String(250))
    __table_args__ = (ForeignKeyConstraint([UserId],['user.id']), {})
    @property
    def serialize(self):
        return {
            'id' : self.contactId,
            'name' : self.name,
            'phoneNumber' : self.phoneNumber,
            'email' : self.email,
            'address' : self.address,
        }


engine = create_engine('sqlite:///phonebook.db')
Base.metadata.bind = engine
DB = sessionmaker(bind=engine)
Base.metadata.create_all()
session = DB()