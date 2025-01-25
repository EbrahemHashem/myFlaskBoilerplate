from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, Integer, ForeignKey, String, Column
from .client_units import ClientUnits
from .deleted_clients import DelClientUnits
from sqlalchemy.orm import backref
import datetime

from .unit_amenity import UnitAmenities
# Alias common DB names
import uuid
Column = Column
Model = db.Model
relationship = db.relationship

class Units(Model):
    __tablename__ = 'units'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    name = Column(String(64))
    village_id = Column(CHAR(36), ForeignKey('villages.id'))
    building_id = Column(CHAR(36), ForeignKey('buildings.id'))
    ext_id = Column(String(64))
    clients = relationship("Client", secondary = 'clients_units', backref=backref("unit"), lazy="joined")
    del_clients = relationship("Client", secondary = DelClientUnits, backref=backref("del_unit"), lazy="dynamic")
    invoices = relationship("Invoice", backref=backref("unit"), lazy=True)
    notes = relationship("Notes", backref=backref("unit"), lazy=True)
    cards = relationship("Cards", backref=backref("unit"), lazy=True)
    qr_codes = relationship("Qr_codes", backref=backref("unit"), lazy=True)
    gate_quota = relationship("GateQuota", backref=backref("unit"), lazy=True)
    quotas = relationship("Quota", backref=backref("unit"), lazy=True)
    type_id = Column(CHAR(36), ForeignKey('types.id'))
    timestamp = Column(db.DateTime, default=datetime.datetime.now)
    gates = relationship("Gates", backref=backref("unit"), uselist= False)
    orders = relationship("ServiceOrder", backref=backref("unit"))
    disabled = Column(BOOLEAN, default=False, index=True)
    amenities = relationship("Amenity", secondary = UnitAmenities, backref=backref("unit"), lazy="dynamic")
    rentals = relationship("UnitBooking", backref=backref("unit"))
    # time_line_tickets = relationship("ServiceOrderTicket", backref=backref("unit"), uselist= False)
    unit_description = relationship("UnitDetails", backref=backref("unit"), uselist= False)
    location = relationship("Location", backref=backref("unit"), uselist= False)

    def __init__(self, **kwargs):
        super(Units, self).__init__(**kwargs)
    
    def to_json(self):

        return{
            "id": self.id,
            "name": self.name,
            "village_id": self.village_id,
            "owners": self.clients
            }
    
    def named(self):

        return{
            "name": self.name,
            }