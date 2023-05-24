from sqlalchemy import Column, DateTime, ForeignKey, Integer, String,Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from source import db


class Groups(db.Model):
    __tablename__ = 'groups'
    idGroup = Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(100), nullable=False)
    describe=Column(Text,nullable=True)
    describe=Column(Text,nullable=True)
    idOwner= Column(Integer,nullable=False)
    createAt=Column(DateTime(timezone=True),default=func.now())
    notes=relationship('Notes',backref='groups',lazy=True, cascade="all, delete")
    