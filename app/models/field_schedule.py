import datetime
from app import db, bcrypt
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, DateTime, Column, Date, ForeignKey, DATETIME, Boolean

from sqlalchemy.orm import backref
# Alias common DB names
import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import relationship
import os

BASE_URL = str(os.environ.get("BASE_URL"))
IMAGE_RETRIEVAL_URL = str(os.environ.get("IMAGE_RETRIEVAL_URL"))
now = datetime.datetime.now()

class FieldSchedule(Model):
    __tablename__ = 'field_schedule'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        

    date = Column(Date, nullable=False)
    time_slots = relationship('TimeSlot', backref=backref('schedule'), lazy=True)
    field_id = Column(CHAR(36), ForeignKey('field.id'), nullable=False)
    created_at = Column(DateTime, default=now)

    def __init__(self, **kwargs):
            super(FieldSchedule, self).__init__(**kwargs)
        
    def to_json(self):

        return{
            "id": self.id,
            "date": str(self.date),
            "slots": [time_slot.to_json() for time_slot in self.time_slots]
        }
