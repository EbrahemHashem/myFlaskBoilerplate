from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, ForeignKey, String, Column
import datetime
from sqlalchemy.orm import backref, relationship
from app.models.user_services import UserServices
import uuid
Column = Column
Model = db.Model
import os

BASE_URL = str(os.environ.get("BASE_URL"))
IMAGE_RETRIEVAL_URL = str(os.environ.get("IMAGE_RETRIEVAL_URL"))

class ServiceOrder(db.Model):
    __tablename__ = 'service_order'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    user_id = Column(CHAR(36), ForeignKey('user.id'))
    total_cost = Column(Integer)
    status = Column(String(50), default='Pending')
    timestamp = Column(db.DateTime, default=datetime.datetime.now)
    invoice = relationship("Invoice", backref=backref("order"), uselist= False)
    unit_id = Column(CHAR(36), ForeignKey('units.id'))
    client_id = Column(CHAR(36), ForeignKey('clients.id'))
    phone_number = Column(String(255))
    description = Column(String(255))
    schedule_id = Column(CHAR(36), ForeignKey('service_schedule.id'))
    # service_id = Column(CHAR(36), ForeignKey('services.id'))

    # Relationships
    services = relationship("Services", secondary ="order_service", backref=backref("order"), lazy="joined")
    images = relationship("Image", backref=backref("order"), lazy=True)
    tickets = relationship("ServiceOrderTicket", backref=backref("order"))  # One ticket for the entire order

    def to_json(self):

        return{
            "id": self.id,
            "client": self.client.name,
            "client_id": self.client.id,
            "unit_id": self.unit.id,
            "unit": self.unit.name,
            "status": self.status,
            "service": {"id": self.services[0].service.id,
                        "name": self.services[0].service.name ,
                        "image": "https://{}{}{}".format(BASE_URL, IMAGE_RETRIEVAL_URL, self.services[0].service.images[0].id) if len(self.services[0].service.images)>0 else '',
                        },
            "image": [image.to_json() for image in self.images if len(self.images)>0 ],
            "user": self.user.to_json() if self.user else None,
            "TimeLines": [services.to_json() for services in self.services_link],
            "total_cost": self.total_cost,
            "phone_number": self.phone_number,
            "invoice": self.invoice.to_client() if self.invoice else None,
            "schedule": self.schedule.to_day_retreival(),
            "timestamp": str(self.timestamp)
            }
    
    def to_list(self):

        return{
            "id": self.id,
            "service": {"id": self.services[0].service.id,
                        "name": self.services[0].service.name ,
                        "image": "https://{}{}{}".format(BASE_URL, IMAGE_RETRIEVAL_URL, self.services[0].service.images[0].id) if len(self.services[0].service.images)>0 else '',
                        },
            "unit_id": self.unit.id,
            "client": self.client.name,
            "client_id": self.client.id,
            "status": self.status,
            "image": ["https://{}{}{}".format(BASE_URL, IMAGE_RETRIEVAL_URL, image.id) for image in self.images if len(self.images)>0 ],
            "unit": self.unit.name,
            "schedule": self.schedule.to_day_retreival(),
            "total_cost": self.total_cost,
            "TimeLines": [services.to_json() for services in self.services_link],
            "timestamp": str(self.timestamp)
            }
    
    def to_message(self):

        return{
            "timestamp": self.timestamp,
            "message": self.message,
            "user_type": self.user_type
            }
    