
import datetime
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, ForeignKey, Column, DATETIME, String

from sqlalchemy.orm import backref
from app import db

import uuid
Column = Column
Model = db.Model
relationship = db.relationship

class EventTicketType(Model):
    __tablename__ = "event_ticket_type"
    event_id = Column(ForeignKey("event.id"), primary_key=True)
    type_id = Column(ForeignKey("types.id"), primary_key=True)
    price = Column(Integer)
    event_tickets = relationship("Event", backref=backref("ticket_types"), lazy=True, viewonly=True)
    ticket_events = relationship("Types", backref=backref("ticket_types"), lazy=True, viewonly=True)
    timestamp = Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, **kwargs):
        super(EventTicketType, self).__init__(**kwargs)
    
