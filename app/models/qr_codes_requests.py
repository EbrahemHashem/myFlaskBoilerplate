import datetime
from app import db, bcrypt
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, BOOLEAN, ForeignKey
from sqlalchemy.orm import backref

# Alias common DB names
import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import relationship

class Qr_codes(Model):
    __tablename__ = 'qr_code'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    customer_name = Column(String(255))
    email = Column(String(255))
    phone_number = Column(String(255))
    qr_code = Column(String(255), index=True)
    qr_type_id = Column(CHAR(36), ForeignKey('types.id'))
    count = Column(Integer)
    used = Column(Integer)
    cancelled = Column(BOOLEAN, default=False, index=True)
    start_time = Column(db.DateTime)
    end_time = Column(db.DateTime)
    customer_id = Column(CHAR(36), ForeignKey('clients.id'))
    unit_id = Column(CHAR(36), ForeignKey('units.id'))
    timestamp = Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, **kwargs):
        super(Qr_codes, self).__init__(**kwargs)
    
    def to_json(self):

        return{
            "qr_code": self.qr_code,
            "customer_name": self.customer_name,
            "phone_number": self.phone_number,
            "qr_type_id": self.type.id,
            "count": self.count,
            "used": self.used,
            "cancelled": False,
            "start_time": str(self.start_time),
            "end_time": str(self.end_time),
            "customer_id": self.client.id,
            "unit_id": self.unit.id,
            "timestamp": str(datetime.datetime.now())
        }