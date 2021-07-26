from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

#SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@<ip/domain_name>:<port>/<database_name>"
# I've set this as an ENV variable now.

engine = create_engine(os.environ.get('SQLALCHEMY_DATABASE_URL'))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()