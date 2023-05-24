from sqlalchemy import Column, DateTime, ForeignKey, Integer, String,Text
from sqlalchemy.sql import func

from source import db
from source.main.model.groups import Groups


class Rooms(db.Model):
    __tablename__ = 'rooms'
    idGroup = Column(Integer,ForeignKey(Groups.idGroup),nullable=False)
    idRoom=Column(String(100), nullable=False,primary_key=True)
    text=Column(Text,nullable=False)
    idSend=Column(Text,nullable=False)
    createAt=Column(DateTime(timezone=True),default=func.now())
   