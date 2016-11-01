from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class user(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary-key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250))  # should be unique

class Contact(Base):
    __tablename__ = 'Contact'
    contactId = Column(Integer, primary-key=True)
    UserId = Column(Integer, foreign-key) #
    name = Column(String)
    phoneNumber = Column(String(20))
    address = Column(String(250))
    email = Column(String(250))
    __table_args__ = (ForeignKeyConstraint([Userid],['user.id']), {})
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
base.metadata.bind = engine
DB = sessinomaker(bind=engine)
session = DB()