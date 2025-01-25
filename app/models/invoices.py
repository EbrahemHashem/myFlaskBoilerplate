import datetime
from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, Integer, Boolean, String, Column, ForeignKey, DateTime, func
from app.models.images import Image
from datetime import datetime as date
relationship = db.relationship
from sqlalchemy.orm import backref

import uuid
Column = Column
Model = db.Model

class Invoice(Model):
    __tablename__ = 'invoice'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    client_id = Column(CHAR(36), ForeignKey('clients.id'))
    promocode_id = Column(CHAR(36), ForeignKey('promocodes.id'))
    unit_id = Column(CHAR(36), ForeignKey('units.id'))
    notifications = relationship("Notifications", backref=backref("invoice"), lazy="joined")
    type_id = Column(CHAR(36), ForeignKey('types.id'))
    payment_type_id = Column(CHAR(36), ForeignKey('types.id'))
    utility_id = Column(CHAR(36), ForeignKey('utility.id'))
    service_id = Column(CHAR(36), ForeignKey('services.id'))
    user_id = Column(CHAR(36), ForeignKey('user.id'))
    payment_user_id = Column(CHAR(36), ForeignKey('user.id'))
    purchase_name = Column(String(255))
    description = Column(String(255))
    paid = Column(Boolean, default=False, index=True)
    delivered = Column(Boolean, default=False, index=True)
    disabled = Column(BOOLEAN, default=False, index=True)
    ammount = Column(Integer)
    consumed = Column(Integer)
    items = relationship("Item", backref=backref("invoice"))
    order_id = Column(CHAR(36), ForeignKey('service_order.id'))  # Changed from service_timeline to service_order
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_on = Column(DateTime, server_default=func.now(), onupdate=func.now())
    invoce_type = relationship('Types', foreign_keys=[type_id], backref='invoce_type')
    payment_type = relationship('Types', foreign_keys=[payment_type_id], backref='payment_type')

    user = relationship('User', foreign_keys=[user_id], backref='user')
    payment_user = relationship('User', foreign_keys=[payment_user_id], backref='payment_user')

    def __init__(self, **kwargs):
        super(Invoice, self).__init__(**kwargs)
    
    def to_json(self):

        return{
            "id": self.id,
            "purchase_name": self.purchase_name,
            "disabled": self.disabled,
            "ammount": self.ammount,
            "description": self.description
            
        }
    
    def to_client(self):

        return{
            "id": self.id,
            "purchase_name": self.purchase_name,
            "ammount": self.ammount,
            "consumed": self.consumed,
            "paid": self.paid,
            "disabled": self.disabled,
            "disabled": self.disabled,
            "items": [item.to_json() for item in self.items if self.items],
            "created_at": str(self.created_at),
            "delivered": self.delivered,
            # "section": self.section() if self.utility.sections else None,
            "updated_on": str(self.updated_on),
            "payment_user": self.payment_user.to_json() if self.payment_user else None,
            "invoce_type": self.invoce_type.to_list()if self.invoce_type else None,
            "payment_type": self.payment_type.to_list()if self.payment_type else None,
            "user": self.user.to_json() if self.user else None,
            "description": self.description
            
        }
    def to_utility(self):

        return{
            "id": self.id,
            "purchase_name": self.purchase_name,
            "ammount": self.ammount,
            "consumed": self.consumed,
            "paid": self.paid,
            "disabled": self.disabled,
            "created_at": str(self.created_at),
            "section": self.section() if self.utility.sections else None,
            "updated_on": str(self.updated_on),
            "description": self.description
            
        }
    def to_invoice(self):

        return{
            "id": self.id,
            "purchase_name": self.purchase_name,
            "ammount": self.ammount,
            "paid": self.paid,
            "disabled": self.disabled,
            "created_at": str(self.created_at),
            "updated_on": str(self.updated_on),
            "description": self.description
            
        }
    
    def section(self):
        for section in self.utility.sections:
            if self.consumed >= section.start and self.consumed <= section.end:
                return section.name