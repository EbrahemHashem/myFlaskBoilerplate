from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, ForeignKey
import datetime

from app.models.event_attendee import EventAttendee
from app.models.event_host import EventHost

import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import backref, relationship

class Event(db.Model):
    __tablename__ = "event"

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    name = Column(String(255))
    start_time = Column(db.DateTime)
    end_time = Column(db.DateTime)
    capacity = Column(Integer)
    location = Column(String(120))
    description = Column(db.Text)
    instructions = Column(db.Text)
    timestamp = Column(db.DateTime, default=datetime.datetime.now)
    ratings = relationship("Ratings", backref=backref("event"), lazy="joined")
    attendees = relationship("Attendee", secondary = EventAttendee, backref=backref("events"), lazy="joined")
    hosts = relationship("Host", secondary = EventHost, backref=backref("events"), lazy="joined")
    event_tickets = relationship("Types", secondary = 'event_ticket_type', backref=backref("events"), lazy="joined")
    notifications = relationship("Notifications", backref=backref("event"), lazy="joined")
    waitinglist = relationship("WaitingList", backref=backref("event"), uselist= False)

    
    tickets = relationship("Ticket", backref="event")
    sponsors = Column(String(120))


    def _init_(self, **kwargs):
        super(Event, self)._init_(**kwargs)
        
    def to_json(self):

        return {
            "id": self.id,
            "name": self.name,
            "start_time": str(self.start_time),
            "end_time": str(self.end_time),
            "capacity": self.capacity,
            "location": self.location,
            "description": self.description,
            "instructions": self.id,
            "host": self.hosts.to_json() if self.hosts else None
            }