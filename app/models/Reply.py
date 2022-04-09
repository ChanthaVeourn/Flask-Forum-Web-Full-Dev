from sqlalchemy import String, Integer, Column, ForeignKey, Table
from sqlalchemy.orm import relationship

from app.models import Base
from .Base_model import BaseModel

association_table = Table(
    'reply_tag',
    Base.metadata,
    Column('reply_id',Integer, ForeignKey('reply.id', ondelete="CASCADE")),
    Column('tag_id',Integer, ForeignKey('tag.id', ondelete="CASCADE"))
)

class Reply(Base, BaseModel):

    __tablename__= "reply"
    title = Column(String(64), nullable=False)
    description = Column(String(1024), nullable=False)
    parent_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    forum_id = Column(Integer, ForeignKey('forum.id'), nullable=False)

    tags = relationship('TagModel', secondary=association_table, backref='replies', lazy=True,
        cascade="all, delete")


    def __init__(self,schema):

        if not isinstance(schema, dict):
            raise ArgumentError("Schema should be a dictionary")

        for attribute, value in schema.items():
            if hasattr(self, attribute) and getattr(self, attribute) != value:
                setattr(self, attribute, value) 