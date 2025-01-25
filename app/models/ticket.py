from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, ForeignKey
import datetime

import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import backref, relationship

class Ticket(db.Model):
    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        

    attendee_id = Column(CHAR(36), ForeignKey('attendee.id'))
    event_id = Column(CHAR(36), ForeignKey('event.id'))
    type_id = Column(CHAR(36), ForeignKey('types.id'))
    price = Column(db.Float)


    def _init_(self, **kwargs):
        super(Ticket, self)._init_(**kwargs)
        
    def to_json(self):

        return {
            "id": self.id,
            "name": self.name
            }