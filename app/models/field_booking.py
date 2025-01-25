import datetime
from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, Column, ForeignKey, DateTime
import os


# Alias common DB names
import uuid
Column = Column
Model = db.Model

BASE_URL = str(os.environ.get("BASE_URL"))
IMAGE_RETRIEVAL_URL = str(os.environ.get("IMAGE_RETRIEVAL_URL"))
now = datetime.datetime.now()

class FieldBooking(Model):
    __tablename__ = 'field_booking'
    
    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    field_id = Column(CHAR(36), ForeignKey('field.id'), nullable=False)
    client_id = Column(CHAR(36), ForeignKey('clients.id'))

    def __init__(self, **kwargs):
            super(FieldBooking, self).__init__(**kwargs)
        
    def to_json(self):

        return{
            "id": self.id,
            "name": self.name,
            "sport": self.sport.name,
            "images": ["https://{}{}{}".format(BASE_URL, IMAGE_RETRIEVAL_URL, image.id) for image in self.images]
        }
