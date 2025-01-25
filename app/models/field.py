import datetime
from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, DateTime, ForeignKey, DATETIME, Boolean
from sqlalchemy.orm import relationship
import os

from sqlalchemy.orm import backref
# Alias common DB names
import uuid
Column = Column
Model = db.Model

BASE_URL = str(os.environ.get("BASE_URL"))
IMAGE_RETRIEVAL_URL = str(os.environ.get("IMAGE_RETRIEVAL_URL"))
now = datetime.datetime.now()

class Field(Model):
    __tablename__ = 'field'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        

    name = Column(String(100), nullable=False)
    sport_id = Column(CHAR(36), ForeignKey('sport.id'), nullable=False)
    is_rented = Column(Boolean, default=False)
    bookings = relationship('FieldBooking', backref=backref('field'), lazy=True)
    images = relationship("Image", backref=backref("field"), lazy=True)
    created_at = Column(DateTime, default=now)

    def __init__(self, **kwargs):
            super(Field, self).__init__(**kwargs)
        
    def to_json(self):

        return{
            "id": self.id,
            "name": self.name,
            "sport": self.sport.name,
            "images": ["https://{}{}{}".format(BASE_URL, IMAGE_RETRIEVAL_URL, image.id) for image in self.images]
        }
