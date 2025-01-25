from app import db
from datetime import datetime
from sqlalchemy.dialects.mysql import LONGBLOB

from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, ForeignKey

import uuid
Column = Column
Model = db.Model

class Ratings(Model):
    __tablename__ = "ratings"
    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    rating = Column(Integer)
    joined_date = Column(db.DateTime, default=datetime.utcnow)
    service_id = Column(CHAR(36), ForeignKey('services.id'))
    client_id = Column(CHAR(36), ForeignKey('clients.id'))
    attendee_id = Column(CHAR(36), ForeignKey('attendee.id'))
    event_id = Column(CHAR(36), ForeignKey('event.id'))

    def __init__(self, **kwargs):
        super(Ratings, self).__init__(**kwargs)

    def to_json(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "joined_date": str(self.joined_date),
            "client": self.client.username
        }
