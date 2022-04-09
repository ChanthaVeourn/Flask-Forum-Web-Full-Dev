from sqlalchemy import String, Integer, Column, ForeignKey

from app.models import Base
from .Base_model import BaseModel

class AddressModel(Base, BaseModel):
    
    __tablename__ = 'address'

    address1 = Column(String(128))
    address2 = Column(String(128))
    city = Column(String(128))
    state = Column(String(128))
    country = Column(String(128))
    zipcode = Column(String(5))

    user_id = Column(Integer, ForeignKey('user.id'), unique = True, nullable = False)

    def __init__(self,schema):

        if not isinstance(schema, dict):
            raise ArgumentError("Schema should be a dictionary")

        for attribute, value in schema.items():
            if hasattr(self, attribute) and getattr(self, attribute) != value:
                setattr(self, attribute, value)  