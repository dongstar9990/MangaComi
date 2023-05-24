from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text

from source import db
from source.main.model.notes import Notes


class Datas(db.Model):
    __tablename__ = 'datas'
    idData = Column(Integer, primary_key=True, autoincrement=True)
    idNote = Column(Integer, ForeignKey(Notes.idNote), nullable=False)
    content = Column(Text)
    doneContent=Column(Boolean, nullable=False, default=0)

   