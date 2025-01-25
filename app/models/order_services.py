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

class OrderService(Model):
    __tablename__ = 'order_service'
    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        

    order_id = Column(CHAR(36), ForeignKey('service_order.id'), primary_key=True)
    service_id = Column(CHAR(36), ForeignKey('services.id'), primary_key=True)
    quantity = Column(Integer)
    cost = Column(Integer)  # You may include cost here if needed

    # Relationships
    order = db.relationship("ServiceOrder", backref=backref("services_link"), lazy=True, viewonly=True)
    service = db.relationship("Services", backref=backref("orders_link"), lazy=True, viewonly=True)

    def __init__(self, **kwargs):
        super(OrderService, self).__init__(**kwargs)
    
    def to_json(self):
        return {
            "service_id": self.service_id,
            "service_name": self.service.name,
            "quantity": self.quantity,
            "cost": self.cost
        }
