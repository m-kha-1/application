from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,Integer,String,Text,Float,Boolean,ForeignKey


import os
from dotenv import load_dotenv

load_dotenv()
p=os.getenv('password')

# sqlalchemy_url = 'postgresql://user:1mispace@localhost/app_database1'
sqlalchemy_url="mysql+pymysql://root:1mispace@localhost/app2"
engine=create_engine(f"mysql+pymysql://root:{p}@localhost/app2", echo=True)
# engine = create_engine(sqlalchemy_url, echo=True)



session = sessionmaker(auticommit=False,bind=engine,autoflush=False)

Base = declarative_base()

# Base.metadata.create_all(bind=engine)