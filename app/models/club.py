import datetime
from app import db, bcrypt
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, Text, ForeignKey, DateTime, Boolean

from sqlalchemy.orm import backref
# Alias common DB names
import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import relationship
import os

BASE_URL = str(os.environ.get("BASE_URL"))
IMAGE_RETRIEVAL_URL = str(os.environ.get("IMAGE_RETRIEVAL_URL"))

now = datetime.datetime.now()

class Club(Model):
    __tablename__ = 'club'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        

    name = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    sports = relationship('Sport', backref='club', lazy=True)
    images = relationship("Image", backref=backref("club"), lazy=True)
    created_at = Column(DateTime, default=now)
    subscriptions = relationship('Subscription', backref=backref('club'), lazy=True)

    def __init__(self, **kwargs):
            super(Club, self).__init__(**kwargs)
        
    def to_json(self):

        return{
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "images": ["https://{}{}{}".format(BASE_URL, IMAGE_RETRIEVAL_URL, image.id) for image in self.images]
        }