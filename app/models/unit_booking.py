from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, ForeignKey, DateTime
import datetime

from app.models.client_booking_periods import ClientRentals

import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import backref, relationship

now = datetime.datetime.now()

class UnitBooking(Model):
    __tablename__ = 'unitbooking'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        

    checkin_date = Column(DateTime, nullable=False, default=now)
    checkout_date = Column(DateTime, nullable=False, default=now)
    rentals = relationship("Client", secondary = ClientRentals, backref=backref("rentals"), lazy="dynamic")
    unit_id = Column(CHAR(36), ForeignKey('units.id'))

    def __init__(self, **kwargs):
        super(UnitBooking, self).__init__(**kwargs)

    def to_json(self):

        return {
            "id": self.id,
            "checkin_date": str(self.checkin_date),
            "checkout_date": str(self.checkout_date),
            # "client_name": self.client.name,
            }