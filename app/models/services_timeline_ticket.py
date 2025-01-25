from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, ForeignKey, String, Column
import datetime
from sqlalchemy.orm import backref, relationship
from app.models.user_services import UserServices
import uuid
Column = Column
Model = db.Model

class ServiceOrderTicket(Model):
    __tablename__ = 'service_timeline_ticket'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    # unit_id = Column(CHAR(36), ForeignKey('units.id'))
    order_id = Column(CHAR(36), ForeignKey('service_order.id'))  # Changed from service_timeline to service_order
    message = Column(db.String(255), nullable=False)
    user_type = Column(db.String(50), nullable=False)
    timestamp = Column(db.DateTime, default=datetime.datetime.now)

    # Relationships
    
    def to_json(self):

        return{
            "id": self.id,
            "message": self.message,
            "user_type": self.user_type,
            "timestamp": self.timestamp.isoformat()
            }
    
    def to_list(self):

        return{
            "timestamp": self.timestamp,
            "message": self.message,
            "user_type": self.user_type
            }
    
    