import datetime
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
from sqlalchemy.orm import backref
from app import db, bcrypt
import os

BASE_URL = str(os.environ.get("BASE_URL"))
IMAGE_RETRIEVAL_URL = str(os.environ.get("IMAGE_RETRIEVAL_URL"))

import uuid
Column = Column
Model = db.Model
relationship = db.relationship

class UserCards(Model):

    __tablename__ = "user_cards"

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    
    type_id = Column(ForeignKey('types.id'), nullable=False)
    project_id = Column(CHAR(36), ForeignKey('projects.id'), nullable=False)
    timestamp = Column(db.DateTime, default=datetime.datetime.now)
    images = relationship("Image", backref=backref("user_card"), lazy=True)

    # __table_args__ = (UniqueConstraint(user_id, village_id, role_id),)

    type = relationship("Types", backref = backref("user_card", uselist=False), uselist=False)
    project = relationship("Projects", backref = backref("user_card"), uselist=False)

    def __init__(self, **kwargs):
        super(UserCards, self).__init__(**kwargs)

    def to_json(self):
        return{
            "id": self.id,
            "type": self.type.name,
            "project": self.project.name,
            "images": self.image_list()
        }
    
    def image_list(self):
        if len(self.images)>0:
            return [image.to_json() for image in self.images]