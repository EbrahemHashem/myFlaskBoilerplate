from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, ForeignKey, String, Column
import datetime

# Alias common DB names
import uuid
Column = Column
Model = db.Model
relationship = db.relationship

class Notes(Model):
    __tablename__ = 'notes'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    user_id = Column(CHAR(36), ForeignKey('user.id'))
    unit_id = Column(CHAR(36), ForeignKey('units.id'))
    note = Column(String(255))
    client_id = Column(CHAR(36), ForeignKey('clients.id'))
    timestamp = Column(db.DateTime, default=datetime.datetime.now)
    expiry_date = Column(db.DateTime)
    action = Column(String(255))

    
    def __init__(self, **kwargs):
        super(Notes, self).__init__(**kwargs)
    
    def to_json(self):

        return{
            "id": self.id,
            "note": self.note           
        }