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

class Amenity(Model):
    __tablename__ = 'amenity'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    name = Column(String(255))
    
    def __init__(self, **kwargs):
        super(Amenity, self).__init__(**kwargs)
    
    def to_json(self):

        return{
            "id": self.id,
            "unit_name": self.name
            }
