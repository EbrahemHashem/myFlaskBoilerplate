import uuid
import datetime
from app import db
from sqlalchemy import  String, Column, Boolean, Text,DateTime
from sqlalchemy.orm import backref,relationship
from app.models.client_requests import ClientRequests
Column = db.Column
Model = db.Model



class Requests(Model):
    __tablename__ = "request"
    id = Column(String(36),primary_key=True,default =lambda:str(uuid.uuid4()),unique = True,nullable = False)
    title = Column(String,nullable =False)
    instruction = Column(Text,nullable =False)
    attached = Column(Boolean,nullable =False)
    signed = Column(Boolean,nullable =False)
    voice_attached = Column(Boolean,nullable =False)
    description =Column(String,nullable =False)
    status =Column(String,nullable = False)
    timestamp = Column(DateTime, default=datetime.datetime.now)
    # 
    clients =relationship('Client',
                          secondary=ClientRequests,
                          
                        #   primaryjoin=id == ClientRequests.c.client_id,
                        #   secondaryjoin=id == ClientRequests.c.request_id,
                          backref=backref("requests"))
    # test =Column(String,nullable = False)ClientsRequests

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "timestamp": str(self.timestamp),
        }

    def __init__(self, **kwargs):
          super(Requests, self).__init__(**kwargs)


