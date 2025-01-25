import datetime
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
from sqlalchemy.orm import backref
from app import db, bcrypt

import uuid
Column = Column
Model = db.Model
relationship = db.relationship

class ClientUnits(Model):
    __tablename__ = "clients_units"
    unit_id = Column(ForeignKey("units.id"), primary_key=True)
    client_id = Column(ForeignKey("clients.id"), primary_key=True)
    relation = Column(String(50))
    client_units = relationship("Client", backref=backref("clients_units"), lazy=True, viewonly=True)
    unit_clients = relationship("Units", backref=backref("clients_units"), lazy=True, viewonly=True)

    # __mapper_args__ = {
    #     "polymorphic_on": type,
    #     "polymorphic_identity": "employee",
    #     }
    def __init__(self, **kwargs):
        super(ClientUnits, self).__init__(**kwargs)
    
    
#     # child = relationship("Child")

# ClientUnits = db.Table('clients_units',
#     Column('time_stamp', DATETIME, default=datetime.datetime.now),
#     Column('unit_id', CHAR(36), ForeignKey("units.id"), primary_key=True),
#     Column('client_id', CHAR(36), ForeignKey("clients.id"), primary_key=True),
#     Column('relation', String(255))
#     )
