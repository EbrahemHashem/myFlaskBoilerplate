from datetime import datetime
from app import db
from sqlalchemy.orm import relationship, backref

from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, ForeignKey, DateTime

import uuid
Column = Column
Model = db.Model
relationship = db.relationship

class PromoCodes(Model):
    __tablename__ = "promocodes"
    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    promo_code = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    percentage = Column(Integer)
    type_id = Column(CHAR(36), ForeignKey('types.id'))
    limit = Column(Integer)
    # service_requests = relationship("ServiceOrder", backref=backref("promocode"), lazy="joined")
    invoices = relationship("Invoice", backref=backref("promocode"))

    
    def __init__(self, **kwargs):
        super(PromoCodes, self).__init__(**kwargs)

    def __repr__(self):
        return f"<{self.name} - {self.id}>"

    def to_json(self):

        return {
            "id": self.id,
            "promo_code": self.promo_code,
            "percentage": self.percentage,
            "limit": self.limit,
            "service_requests": [service_request.to_promo() for service_request in self.service_requests]            
        }

    def to_invoice(self):

        return {
            "id": self.id,
            "promo_code": self.promo_code,
            "percentage": self.percentage,
            "limit": self.limit,
            "Invoices": [invoice.to_client() for invoice in self.invoices]            
        }
