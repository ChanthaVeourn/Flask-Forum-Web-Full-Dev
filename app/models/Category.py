from sqlalchemy import String, Integer, Column

from app.models import Base
from .Base_model import BaseModel
from app.utils.slash_helper import sanitize_key


class Category(Base, BaseModel):
    __tablename__= 'category'
    
    title = Column(String(length=30), nullable=False )
    description = Column(String(length=1024), nullable=False)
    slush = Column(String(128))
    def __repr__(self):
        return f'title:{self.title} body:{self.body}'

    def __init__(self,schema):

        if not isinstance(schema, dict):
            raise ArgumentError("Schema should be a dictionary")

        for attribute, value in schema.items():
            if hasattr(self, attribute) and getattr(self, attribute) != value:
                setattr(self, attribute, value) 
        if not self.slush:
            self.slush = sanitize_key(self.title)