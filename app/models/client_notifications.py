from app import db
from sqlalchemy.dialects.mysql import LONGBLOB

from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, Column, ForeignKey, BOOLEAN
from sqlalchemy.orm import backref, relationship

import uuid
Column = Column
Model = db.Model

class Client_notifications(Model):
    __tablename__ = "client_notifications"
    client_id = Column(CHAR(36), ForeignKey('clients.id'), primary_key=True)
    notification_id = Column(CHAR(36), ForeignKey('notifications.id'), primary_key=True)
    read = Column(BOOLEAN, default=False, index=True)
    clients = relationship("Client", backref=backref("client_notifications"), viewonly=True)
    notifications = relationship("Notifications", backref=backref("client_notifications"), viewonly=True)

    def __init__(self, **kwargs):
        super(Client_notifications, self).__init__(**kwargs)

    def to_json(self):
        return {
            "id": self.id
        }
    
    # def to_notification(self):
    #     return {
    #         "notification": self.id
    #     }
