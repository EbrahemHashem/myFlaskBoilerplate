import datetime
from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, Integer, String, Column, ForeignKey, DateTime
relationship = db.relationship
from sqlalchemy.orm import backref
import os

BASE_URL = str(os.environ.get("BASE_URL"))
IMAGE_RETRIEVAL_URL = str(os.environ.get("IMAGE_RETRIEVAL_URL"))

import uuid
Column = Column
Model = db.Model
now = datetime.datetime.now()

class Utilities(Model):
    __tablename__ = 'utility'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    # type_id = Column(CHAR(36), ForeignKey('types.id'))
    project_id = Column(CHAR(36), ForeignKey('projects.id'))
    name = Column(String(255))
    unit_measure = Column(String(255))
    invoices = relationship("Invoice", backref=backref("utility"))
    sections = relationship("UtilitiesٍSections", backref=backref("utility"))
    created_at = Column(DateTime, default=now)
    updated_on = Column(DateTime, onupdate=now)
    images = relationship("Image", backref=backref("utility"), lazy=True)
    disabled = Column(BOOLEAN, default=False, index=True)
    notifications = relationship("Notifications", backref=backref("utility"), lazy="joined")

    def __init__(self, **kwargs):
        super(Utilities, self).__init__(**kwargs)
    
    def to_json(self):

        return{
            "id": self.id,
            "name": self.name,
            "unit_measure": self.unit_measure,
            "sections": [section.to_json() for section in self.sections],
            "image": "https://{}{}{}".format(BASE_URL, IMAGE_RETRIEVAL_URL, self.images[0].id) if len(self.images)>0 else '',
        }
     
    