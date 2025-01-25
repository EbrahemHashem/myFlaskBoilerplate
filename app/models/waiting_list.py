from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, ForeignKey
import datetime

import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import backref, relationship

class WaitingList(Model):
    _tablename_ = 'waitinglist'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    # attendee_id = Column(CHAR(36), db.ForeignKey('attendee.id'))
    event_id = Column(CHAR(36), db.ForeignKey('event.id'))
    timestamp = Column(db.DateTime, default=datetime.datetime.now)

    def _init_(self, **kwargs):
        super(WaitingList, self)._init_(**kwargs)
        
    def to_json(self):

        return {
            "id": self.id,
            "name": self.name
            }