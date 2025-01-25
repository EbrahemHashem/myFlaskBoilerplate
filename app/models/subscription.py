import datetime
from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, Column, ForeignKey, DateTime

# Alias common DB names
import uuid
Column = Column
Model = db.Model
now = datetime.datetime.now()


class Subscription(Model):
    __tablename__ = 'subscription'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        

    start_date = Column(DateTime, nullable=False, default=now)
    end_date = Column(DateTime, nullable=False)
    client_id = Column(CHAR(36), ForeignKey('clients.id'))
    club_id = Column(CHAR(36), ForeignKey('club.id'), nullable=False)
    created_at = Column(DateTime, default=now)

    def __init__(self, **kwargs):
            super(Subscription, self).__init__(**kwargs)
        
    def to_json(self):

        return{
            "id": self.id,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
            "name": self.name,
            "fields": [field.to_json() for field in self.fields]
        }
