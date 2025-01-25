import datetime
from app import db, bcrypt
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, BOOLEAN, ForeignKey, DATETIME
from sqlalchemy.orm import backref

# Alias common DB names
import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import relationship

class Quota(Model):
    __tablename__ = 'quota'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    priority = Column(Integer)
    quota = Column(Integer)
    used = Column(Integer)
    day = Column(String(64))
    valid_from = Column(DATETIME)
    valid_to = Column(DATETIME)
    unit_id = Column(CHAR(36), ForeignKey('units.id'))
    timestamp = Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, **kwargs):
        super(Quota, self).__init__(**kwargs)
    
    def to_json(self):

        return{
            "id": self.id,
            "quota": self.quota,
            "unit_id": self.unit_id,
            "used": self.used,
            "priority": self.priority
        }