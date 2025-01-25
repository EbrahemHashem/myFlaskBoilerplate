import datetime
from app import db, bcrypt
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship
import os

# Alias common DB names
import uuid
Column = Column
Model = db.Model

BASE_URL = str(os.environ.get("BASE_URL"))
IMAGE_RETRIEVAL_URL = str(os.environ.get("IMAGE_RETRIEVAL_URL"))
now = datetime.datetime.now()

class Sport(Model):
    __tablename__ = 'sport'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        

    name = Column(String(100), nullable=False)
    club_id = Column(CHAR(36), ForeignKey('club.id'), nullable=False)
    fields = relationship('Field', backref=backref('sport'), lazy=True)
    created_at = Column(DateTime, default=now)

    def __init__(self, **kwargs):
            super(Sport, self).__init__(**kwargs)
        
    def to_json(self):

        return{
            "id": self.id,
            "name": self.name,
            "fields": [field.to_json() for field in self.fields]
        }
