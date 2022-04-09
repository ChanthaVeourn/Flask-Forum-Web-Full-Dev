from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship


from flask_login import UserMixin
from app.models import Base
from .Base_model import BaseModel
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(Base, BaseModel, UserMixin):
    
    __tablename__ = 'user'
    name = Column(String(32), unique=True, nullable=False)
    email = Column(String(128), unique = True, nullable = False)
    password_hash = Column(String(256), nullable=False)

    forums = relationship('Forum', backref='owner', lazy=True)
    
    address = relationship('AddressModel', backref='user', uselist=False, lazy=True)
    
    replies = relationship("Reply", backref='user', lazy=True)
    def __init__(self,schema):

        if not isinstance(schema, dict):
            raise ArgumentError("Schema should be a dictionary")

        for attribute, value in schema.items():
            if hasattr(self, attribute) and getattr(self, attribute) != value:
                setattr(self, attribute, value) 
                                                

    @property
    def password(self):    
        return self.password_hash

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')