import datetime
from app import db, bcrypt
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Text, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, BOOLEAN, ForeignKey, DATETIME, Boolean

from sqlalchemy.orm import backref
# Alias common DB names
import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import relationship

class Client(Model):
    __tablename__ = 'clients'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    name = Column(String(255))
    printed_id = Column(String(255))
    ext_id = Column(String(255))
    firebase_token = Column(Text)
    arabic_name = Column(String(255))
    national_id = Column(String(255))
    birth_date = Column(db.DateTime)
    gender = Column(String(255))
    phone_number = Column(String(255))
    email = Column(String(255))
    password_hash = Column(String(128))
    timestamp = Column(db.DateTime, default=datetime.datetime.now)
    blacklisted_gates = relationship("BlackList", backref=backref("client"), lazy=True)
    cards = relationship("Cards", backref=backref("client"))
    whitelisted_gates = relationship("WhiteList", backref=backref("client"), lazy=True)
    verified = Column(Boolean, default=False, index=True)
    blacklisted = Column(BOOLEAN, default=False, index=True)
    cancelled = Column(BOOLEAN, default=False, index=True)
    deleted = Column(BOOLEAN, default=False, index=True)
    activated = Column(BOOLEAN, default=False, index=True)
    printed = Column(BOOLEAN, default=False, index=True)
    mobile_login = Column(BOOLEAN, default=False, index=True)
    valid_from = Column(DATETIME)
    valid_to = Column(DATETIME)
    invoice = relationship("Invoice", backref=backref("client"))
    notes = relationship("Notes", backref=backref("client"), lazy=True)
    images = relationship("Image", backref=backref("client"), lazy="joined")
    type_id = Column(CHAR(36), ForeignKey('types.id'))
    relation = Column(String(64))
    qr_codes = relationship("Qr_codes", backref=backref("client"), lazy=True)
    ratings = relationship("Ratings", backref=backref("client"), lazy="joined")
    subscriptions = relationship('Subscription', backref='client', lazy=True)
    bookings = relationship('FieldBooking', backref='client', lazy=True)
    orders = relationship("ServiceOrder", backref=backref("client"))

    def __init__(self, **kwargs):
        super(Client, self).__init__(**kwargs)
    
    def to_json(self):

        return{
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "email": self.email,
            "activated": self.activated,
            "phone_number": self.phone_number,
            "valid_from": self.valid_from,
            "valid_to": self.valid_to
        }
    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    