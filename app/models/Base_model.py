from sqlalchemy import String, Integer, Column, DateTime, func

class BaseModel():
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, default = func.now())
    updated_date = Column(DateTime, onupdate = func.now())