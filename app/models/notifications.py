from app import db
from datetime import datetime
from sqlalchemy.dialects.mysql import LONGBLOB

from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, ForeignKey, BOOLEAN
from sqlalchemy.orm import backref, relationship

import uuid
Column = Column
Model = db.Model

class Notifications(Model):
    __tablename__ = "notifications"
    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    title = Column(String(255))
    content = Column(String(255))
    image = relationship('Image', backref='notification', lazy=True, uselist=False)
    joined_date = Column(db.DateTime, default=datetime.utcnow)
    service_id = Column(CHAR(36), ForeignKey('services.id'))
    utility_id = Column(CHAR(36), ForeignKey('utility.id'))
    invoice_id = Column(CHAR(36), ForeignKey('invoice.id'))
    event_id = Column(CHAR(36), ForeignKey('event.id'))

    clients = db.relationship('Client', secondary='client_notifications', backref=backref("notifications"))

    def __init__(self, **kwargs):
        super(Notifications, self).__init__(**kwargs)

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "images": self.image.to_json()['image'] if self.image else None
        }
