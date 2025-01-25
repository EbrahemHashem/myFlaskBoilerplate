from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, ForeignKey
import datetime
from app import db, bcrypt

import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import backref, relationship

class Attendee(db.Model):
    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    full_name = Column(String(120))
    phone_number = Column(String(20))
    device_id = Column(String(20))
    password_hash = Column(String(128))
    images = relationship("Image", backref=backref("attendee"), lazy=True)
    tickets = relationship("Ticket", backref=backref("attendee"), lazy="joined")
    event_id = Column(CHAR(36), ForeignKey('event.id'))
    ratings = relationship("Ratings", backref=backref("attendee"), lazy="joined")
    timestamp = Column(db.DateTime, default=datetime.datetime.now)


    def _init_(self, **kwargs):
        super(Attendee, self)._init_(**kwargs)
        
    def to_json(self):

        return {
            "id": self.id,
            "phone_number": self.phone_number,
            "images": self.images,
            "id": self.id,
            "full_name": self.full_name
            }
    
    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    