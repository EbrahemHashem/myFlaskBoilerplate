from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, ForeignKey, DATETIME
import datetime

import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import backref, relationship

class Item(db.Model):
    __tablename__ = 'item'
    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        

    name = Column(String(120))
    timestamp = Column(DATETIME, default=datetime.datetime.now)
    invoice_id = Column(CHAR(36), ForeignKey('invoice.id'))
    amount = Column(Integer)
    price = Column(Integer)
    total_price = Column(Integer)


    def _init_(self, **kwargs):
        super(Item, self)._init_(**kwargs)
        
    def to_json(self):

        return {
            "id": self.id,
            "name": self.name,
            "amount": self.amount,
            "price": self.price,
            "total_price": self.total_price,
            }