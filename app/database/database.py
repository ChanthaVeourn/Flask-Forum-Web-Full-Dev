from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session

engine = create_engine('postgresql://postgres:admin@localhost:5432/forum_db', echo = True)

session = scoped_session(sessionmaker(engine))

Base = declarative_base()

Base.query = session.query_property()
