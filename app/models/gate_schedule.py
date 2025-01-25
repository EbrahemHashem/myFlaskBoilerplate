from sqlalchemy.sql.schema import ForeignKey
from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, BOOLEAN, ForeignKey, TIME, DATE
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
import datetime

import uuid
Column = Column
Model = db.Model

class GateSchedule(Model):
    __tablename__ = 'gateschedule'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    gate_id = Column(CHAR(36), ForeignKey('gates.id'))
    start_time = Column(TIME)
    end_time = Column(TIME)
    start_date = Column(DATE)
    end_date = Column(DATE)
    status = Column(BOOLEAN, default=False, index=True)
    user_type_id = Column(CHAR(36), ForeignKey('types.id'))
    schedulers = relationship("Scheduler", backref=backref("schedule"))
    timestamp = Column(db.DateTime, default=datetime.datetime.now)


    def __init__(self, **kwargs):
        super(GateSchedule, self).__init__(**kwargs)

        
    def to_json(self):

        return {
            "id": self.id,
            }