from argparse import ArgumentError
from sqlalchemy import String, Integer, Column, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.models import Base
from .Base_model import BaseModel
from app.utils.slash_helper import sanitize_key

class TagModel(Base, BaseModel):
    
    __tablename__ = 'tag'
    
    name = Column(String(64), nullable = False, unique=True)
    slush = Column(String(128))
    description = Column(String(256))

    def __init__(self,schema):

        if not isinstance(schema, dict):
            raise ArgumentError("Schema should be a dictionary")

        for attribute, value in schema.items():
            if hasattr(self, attribute) and getattr(self, attribute) != value:
                setattr(self, attribute, value)    
        if not self.slush:
            self.slush = sanitize_key(self.name)