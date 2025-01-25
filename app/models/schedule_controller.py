import datetime
from app import db, bcrypt
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, BOOLEAN, ForeignKey
from sqlalchemy.orm import backref

# Alias common DB names
import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import relationship

class Scheduler(Model):
    __tablename__ = 'scheduler'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    status = Column(BOOLEAN, default=False, index=True)
    tech_id = Column(CHAR(36), ForeignKey('types.id'))
    schedule_id = Column(CHAR(36), ForeignKey('gateschedule.id'))
    timestamp = Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, **kwargs):
        super(Scheduler, self).__init__(**kwargs)
    
    def to_json(self):

        return{
            "id": self.id,
            "status": self.status
        }