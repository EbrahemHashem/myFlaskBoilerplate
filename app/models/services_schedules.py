from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, ForeignKey, String, Column, DATE, TIME
from sqlalchemy.orm import backref
import datetime

import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import relationship

class ServiceSchedule(Model):
    __tablename__ = 'service_schedule'

    """ Services model for adding new services """

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    service_id = Column(CHAR(36), ForeignKey('services.id'))
    capacity = Column(Integer)
    day = Column(DATE)
    start = Column(TIME)
    end = Column(TIME)
    timestamp = Column(db.DateTime, default=datetime.datetime.now)

    orders = relationship("ServiceOrder", backref=backref("schedule"))

    def __init__(self, **kwargs):
        super(ServiceSchedule, self).__init__(**kwargs)

    def to_json(self):

        return{
            "id": self.id,
            "day": str(self.day),
            "start": str(self.start),
            "end": str(self.end),
            "capacity": self.capacity
        }

    def to_service(self):

        return{
            "id": self.id,
            "day": str(self.day),
            "start": str(self.start),
            "end": str(self.end)
        }

    def to_day_retreival(self):

        return str(self.day) + " From: " + str(self.start) + " To: " + str(self.end)