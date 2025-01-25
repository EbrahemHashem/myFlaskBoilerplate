import datetime
from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, ForeignKey, DateTime
from app.models.images import Image
from datetime import datetime as date
relationship = db.relationship
from sqlalchemy.orm import backref

import uuid
Column = Column
Model = db.Model
now = datetime.datetime.now()
class UtilitiesٍSections(Model):
    __tablename__ = 'section'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    name = Column(String(255))
    start = Column(Integer)
    end = Column(Integer)
    price = Column(Integer)
    utility_id = Column(CHAR(36), ForeignKey('utility.id'))
    created_at = Column(DateTime, default=now)
    updated_on = Column(DateTime, onupdate=now)

    def __init__(self, **kwargs):
        super(UtilitiesٍSections, self).__init__(**kwargs)
    
    def to_json(self):

        return{
            "id": self.id,
            "name": self.name,
            "start": self.start,
            "end": self.end,
            "price": self.price,
            "created_at": str(self.created_at),
            "updated_on": str(self.updated_on),
        }