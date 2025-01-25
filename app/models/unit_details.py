from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, ForeignKey, Boolean
import os

from sqlalchemy.orm import backref
# Alias common DB names
import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import relationship

BASE_URL = str(os.environ.get("BASE_URL"))
IMAGE_RETRIEVAL_URL = str(os.environ.get("IMAGE_RETRIEVAL_URL"))

class UnitDetails(Model):
    __tablename__ = 'unit_description'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    floor = Column(String(64))
    bath = Column(String(64))
    beds = Column(String(64))
    rooms = Column(String(64))
    area = Column(String(64))
    unit_measure = Column(String(64))
    gardened = Column(Boolean, default=False, index=True)
    delivered = Column(Boolean, default=False, index=True)
    available_for_rent = Column(Boolean, default=False, index=True)
    garden_area = Column(String(255))
    min_capacity = Column(String(64))
    max_capacity = Column(String(64))
    price_per_night = Column(String(64))
    currency = Column(String(64))
    images = relationship("Image", backref=backref("unit_description"), lazy=True)
    type_id = Column(CHAR(36), ForeignKey('types.id'))
    unit_id = Column(CHAR(36), ForeignKey('units.id'))

    def __init__(self, **kwargs):
        super(UnitDetails, self).__init__(**kwargs)
    
    def to_json(self):

        return{
            "id": self.id,
            "unit_name": self.unit.name,
            "beds": self.beds,
            "floor": self.floor,
            "bath": self.bath,
            "rooms": self.rooms,
            "area": self.area,
            "unit_measure": self.unit_measure,
            "gardened": self.gardened,
            "garden_area": self.garden_area,
            "delivered": self.delivered,
            "location": self.unit.location.to_json() if self.unit.location else None,
            "min_capacity": self.min_capacity,
            "max_capacity": self.max_capacity,
            "type": self.type.to_list(),
            "images": [image.to_json() for image in self.images]
        }
    
     
    
    