from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://root:1mispace@localhost/app_database1"

engine=create_engine(SQLALCHEMY_DATABASE_URL)

sessionlocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()