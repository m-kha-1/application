from database import Base
from sqlalchemy import Column,Integer,String,Text,Float,Boolean,ForeignKey
class Post(Base):
    
    __tablename__ = 'posts'
    
    id=Column(Integer,primary_key=True)
    title=Column(String(50))
    content=Column(String(50))
    published=Column(Boolean(50))