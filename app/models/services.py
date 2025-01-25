from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, Integer, ForeignKey, String, Column
from sqlalchemy.orm import backref
import datetime
import os

BASE_URL = str(os.environ.get("BASE_URL"))
IMAGE_RETRIEVAL_URL = str(os.environ.get("IMAGE_RETRIEVAL_URL"))

import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import relationship

class Services(Model):
    __tablename__ = 'services'

    """ Services model for adding new services """

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    cost = Column(Integer)
    name = Column(String(255))
    parent_id = Column(CHAR(36), ForeignKey('services.id'))
    disabled = Column(BOOLEAN, default=False, index=True)
    children = relationship("Services",
                    backref=backref("service", remote_side=id),
                    lazy="joined",
                    )
    timestamp = Column(db.DateTime, default=datetime.datetime.now)
    
    # orders = relationship("ServiceOrder", backref=backref("service"))
    shecules = relationship("ServiceSchedule", backref=backref("service"))
    ratings = relationship("Ratings", backref=backref("service"), lazy="joined")
    notifications = relationship("Notifications", backref=backref("service"), lazy="joined")
    images = relationship("Image", backref=backref("service"), lazy=True)
    # invoices = relationship("Invoice", backref=backref("service"))

    def __init__(self, **kwargs):
        super(Services, self).__init__(**kwargs)

    def to_json(self):

        return{
            "id": self.id,
            "cost": self.cost,
        }
        
    def service_data(service):
        json_service = service.type.to_service()
        return{
            'name': json_service['name'],
            'image': json_service['image']
        }
    
    def to_service(self):
        return{
            "id": self.id,
            "name": self.name,
            "parent_id": self.parent_id,
            "image": "https://{}{}{}".format(BASE_URL, IMAGE_RETRIEVAL_URL, self.images[0].id) if len(self.images)>0 else '',
            "children": [child.to_services() for child in self.children]
        }
    
    def to_services(self):
        return{
            "id": self.id,
            "name": self.name,
            "parent_id": self.parent_id,
            "image": "https://{}{}{}".format(BASE_URL, IMAGE_RETRIEVAL_URL, self.images[0].id) if len(self.images)>0 else '',
        }
    
    def to_service_time_line(self):
        return{
            "id": self.id,
            "name": self.name,
            "image": "https://{}{}{}".format(BASE_URL, IMAGE_RETRIEVAL_URL, self.images[0].id) if len(self.images)>0 else ''
        }
    
    def micro_service(self):
        return{
            "id": self.id,
            "name": self.name,
            "cost": self.cost,
            "parent_id": self.parent_id,
            "image": "https://{}{}{}".format(BASE_URL, IMAGE_RETRIEVAL_URL, self.images[0].id) if len(self.images)>0 else '',
        }
    
    