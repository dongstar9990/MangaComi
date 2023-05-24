from source import db
from sqlalchemy import Column,String,Integer,DateTime,Float
from sqlalchemy.orm import relationship
import datetime
import jwt
from sqlalchemy.sql import func
from source import app


class Users(db.Model):
    __tablename__ = 'users'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(100))
    gmail=Column(String(70))
    user_name=Column(String(50))
    password_hash=Column(String(200),nullable=False)
    password_hash_2=Column(String(200),nullable=True)
    notes=relationship('Notes',backref='users',lazy=True, cascade="all, delete")
    r=Column(Integer,nullable=False,default=255)
    g=Column(Integer,nullable=False,default=125)
    b=Column(Integer,nullable=False,default=125)
    a=Column(Float,nullable=False,default=0.87)
    df_screen=Column(String(20),default="Archived")
    df_fontsize=Column(String(20),default="Default") 
    createAt=Column(DateTime(timezone=True),default=func.now())