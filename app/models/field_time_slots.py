import datetime
from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, DateTime, Column, Time, ForeignKey, DATETIME, Boolean
import os

# Alias common DB names
import uuid
Column = Column
Model = db.Model
now = datetime.datetime.now()

BASE_URL = str(os.environ.get("BASE_URL"))
IMAGE_RETRIEVAL_URL = str(os.environ.get("IMAGE_RETRIEVAL_URL"))

class TimeSlot(Model):
    __tablename__ = 'time_slot'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        

    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    is_available = Column(Boolean, default=True)
    schedule_id = Column(CHAR(36), ForeignKey('field_schedule.id'), nullable=False)
    created_at = Column(DateTime, default=now)

    def __init__(self, **kwargs):
            super(TimeSlot , self).__init__(**kwargs)
        
    def to_json(self):

        return{
            "id": self.id,
            "start_time": str(self.start_time),
            "end_time": str(self.end_time),
            "is_available": self.is_available,
        }
