from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, ForeignKey, Boolean
import os
from geoalchemy2 import Geometry
from shapely import wkb

from sqlalchemy.orm import backref
# Alias common DB names
import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import relationship

BASE_URL = str(os.environ.get("BASE_URL"))
IMAGE_RETRIEVAL_URL = str(os.environ.get("IMAGE_RETRIEVAL_URL"))

class Location(Model):
    __tablename__ = 'location'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    country = Column(String(255))
    governorate = Column(String(255))
    city = Column(String(255))
    street = Column(String(255))
    unit_id = Column(CHAR(36), ForeignKey('units.id'))
    # location = Column(Geometry(geometry_type='POINT', srid=4326, spatial_index=True), nullable=False)

    def __init__(self, **kwargs):
        super(Location, self).__init__(**kwargs)
    
    def to_json(self):

        return{
            "id": self.id,
            "country": self.country,
            "governorate": self.governorate,
            "city": self.city,
            "street": self.street,
            # "location": str(wkb.loads((bytes.fromhex(str(self.location)))))
        }
    
     
    # bytes_data = bytes.fromhex(hex_string)

# Use Shapely to convert Well-Known Binary (WKB) to a Point
    # point = wkb.loads(bytes_data)

# Extract coordinates
    # point_coords = point.coords[0]

    