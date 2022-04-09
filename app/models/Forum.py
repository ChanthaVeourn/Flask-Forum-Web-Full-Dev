from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship


from app.models import Base
from .Base_model import BaseModel
from app.utils.slash_helper import sanitize_key

class Forum(Base, BaseModel):
    
    __tablename__ = 'forum'
    
    title = Column(String(length=128), nullable=False, unique=True)
    description = Column(String(length=1024), nullable=False, unique=False)
    slush = Column(String(128))
    owner_id = Column(Integer,ForeignKey('user.id'), nullable=False)
    replies = relationship('Reply', backref='forum', lazy=True)

    def __repr__(self):
        return f'Title:{self.title} Desc:{self.description}' 
  
    def __init__(self,schema):

        if not isinstance(schema, dict):
            raise ArgumentError("Schema should be a dictionary")

        for attribute, value in schema.items():
            if hasattr(self, attribute) and getattr(self, attribute) != value:
                    setattr(self, attribute, value) 

        if not self.slush:
           self.slush = sanitize_key(self.title)
