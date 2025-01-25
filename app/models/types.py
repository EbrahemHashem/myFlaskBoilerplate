import datetime
from app import db, bcrypt
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, BOOLEAN, ForeignKey
from sqlalchemy.orm import backref
from sqlalchemy.orm.collections import attribute_mapped_collection
import os

BASE_URL = str(os.environ.get("BASE_URL"))
IMAGE_RETRIEVAL_URL = str(os.environ.get("IMAGE_RETRIEVAL_URL"))

from flask_jwt_extended import get_jwt

from app.models.cards import Cards
# Alias common DB names
import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import relationship

class Types(Model):
    __tablename__ = 'types'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    name = Column(String(64))
    parent_id = Column(CHAR(36), ForeignKey('types.id'))
    children = relationship("Types",
                            # cascade deletions
                    cascade="all, delete-orphan",
                    backref=backref("parent", remote_side=id),
                    lazy="joined",
                    )
    users = relationship("User", backref=backref("type"), lazy=True)
    schedule = relationship("GateSchedule", backref=backref("type"), lazy=True)
    clients = relationship("Client", backref=backref("type"), lazy=True)
    limiters = relationship("Scheduler", backref=backref("type"), lazy=True)
    units = relationship("Units", backref=backref("type"), lazy=True)
    unit_details = relationship("UnitDetails", backref=backref("type"), lazy=True)
    gates = relationship("Gates", backref=backref("type"), lazy=True)
    Cards = relationship("Cards", backref=backref("type"), lazy=True)
    qr_codes = relationship("Qr_codes", backref=backref("type"), lazy=True)
    promocodes = relationship("PromoCodes", backref=backref("type"), lazy=True)
    disabled = Column(BOOLEAN, default=False, index=True)
    deleted = Column(BOOLEAN, default=False, index=True)

    timestamp = Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, **kwargs):
        super(Types, self).__init__(**kwargs)
    
    def to_json(self):
        claims = get_jwt()
        if claims["app"]:
            # if not self.disabled:
            #     koko = {
            #         "id": self.id,
            #         "name": self.name,
            #         "parent_id": self.parent_id,
            #         "children": [child.to_json() for child in self.children]    
            #         }
                return{
                "id": self.id,
                "name": self.name,
                "parent_id": self.parent_id,
                "children": [child.to_json() for child in self.children if not child.disabled]
            } 
        if claims["web"]:
    
            return{
                "id": self.id,
                "name": self.name,
                "parent_id": self.parent_id,
                "children": [child.to_json() for child in self.children]
            }
    def to_list(self):

        return{
            "id": self.id,
            "name": self.name,
            "parent_id": self.parent_id,
        }
    def to_service(self):
        return{
            "id": self.id,
            "name": self.name,
            "parent_id": self.parent_id,
            "image": "https://{}{}{}".format(BASE_URL, IMAGE_RETRIEVAL_URL, self.images[0].id) if len(self.images)>0 else '',
            "children": [child.to_service() for child in self.children]
        }
    def to_name(self):

        return{
            "name": self.name
        }
    def dump(self, _indent=0):
        return ([(c.dump(_indent + 1), c) for c in self.children]
        )
    def dumps(self, _indent=0):
        tree = []

        for c in self.children:
            sub_tree = []
            sub_tree.append(c)
            print(c)
            print(sub_tree)
            tree.append(sub_tree)
            c.dumps(_indent + 1)
        print(tree)
        return tree
    
    
    def micro_service(self):
        json_service = {
            "name": self.name,
            "image": "https://{}{}{}".format(BASE_URL, IMAGE_RETRIEVAL_URL, self.images[0].id) if len(self.images)>0 else '',
            "service": self.service[0].to_json() if len(self.service)>0 else ''
        }
        service_data = json_service['service']
        json_service.pop('service')
        json_service.update(service_data)
        return json_service
    
    def service_data(service):
        json_service = service.type.to_service()
        return{
            'name': json_service['name'],
            'image': json_service['image']
        }
    