from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, ForeignKey, DateTime
import datetime

import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import backref, relationship

now = datetime.datetime.now()

class UnitRentalBooking(Model):
    __tablename__ = 'unit_available_booking'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        

    start_date = Column(DateTime, nullable=False, default=now)
    end_date = Column(DateTime, nullable=False, default=now)
    unit_id = Column(CHAR(36), ForeignKey('units.id'))

    def __init__(self, **kwargs):
        super(UnitRentalBooking, self).__init__(**kwargs)

    def to_json(self):

        return {
            "id": self.id
            # "checkin_date": str(self.checkin_date),
            # "checkout_date": str(self.checkout_date),
            # "client_name": self.client.name,
            # "unit_name": self.unit.name
            }