from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base  # a function inherited for creating the db models
from sqlalchemy.orm import sessionmaker

"""
Template for connecting to a local DB: 
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

Template for connecting to a DB server: 
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = "postgresql://username:password@ip-address/hostname/db_name"
"""

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password321@localhost/fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

"""
Now use the SessionLocal class we created in the database.py file to create a dependency.
We need to have an independent database session/connection (SessionLocal) per request, use the same session through all the request and then close it after the request is finished.
And then a new session will be created for the next request.
Our dependency will create a new SQLAlchemy SessionLocal that will be used in a single request, and then close it once the request is finished.
"""


# Dependency: this creates a session to the DB whenever there is request to the DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()