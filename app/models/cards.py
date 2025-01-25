import datetime
from app import db, bcrypt
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, BOOLEAN, ForeignKey, DATETIME
from sqlalchemy.orm import backref
# Alias common DB names
import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import relationship

class Cards(Model):
    __tablename__ = 'cards'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    card_id = Column(String(255))
    type_id = Column(CHAR(36), ForeignKey('types.id'))
    unit_id = Column(CHAR(36), ForeignKey('units.id'))
    client_id = Column(CHAR(36), ForeignKey('clients.id'))
    license_plate =Column(String(255))
    serial_number =Column(String(255))
    blocked = Column(BOOLEAN, default=False, index=True)
    timestamp = Column(db.DateTime, default=datetime.datetime.now)
    expiry_date = Column(db.DateTime)

    def __init__(self, **kwargs):
        super(Cards, self).__init__(**kwargs)
    
    def to_json(self):

        return{
            "id": self.id,
            "card_id": self.card_id,
            "type_id": self.type_id
        }
    
    def to_client(self):

        return{
            "id": self.id,
            "card_id": self.card_id,
            "serial_number": self.serial_number,
            "blocked": self.blocked,
            "license_plate": self.license_plate,
            "type_id": self.type_id,
            "type_name": self.type.name,
            "expiry_date": self.expiry_date
        }