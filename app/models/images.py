import datetime
import os
from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, ForeignKey, DateTime, Text
from sqlalchemy.dialects.mysql import BLOB
# Alias common DB names
import uuid
Column = Column
Model = db.Model

BASE_URL = str(os.environ.get("BASE_URL"))
IMAGE_RETRIEVAL_URL = str(os.environ.get("IMAGE_RETRIEVAL_URL"))

class Image(Model):
    __tablename__ = 'images'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    path = Column(String(255))
    image = Column(BLOB)
    client_id = Column(CHAR(36), ForeignKey('clients.id'))
    attendee_id = Column(CHAR(36), ForeignKey('attendee.id'))
    order_id = Column(CHAR(36), ForeignKey('service_order.id'))
    service_id = Column(CHAR(36), ForeignKey('services.id'))
    utility_id = Column(CHAR(36), ForeignKey('utility.id'))
    notification_id = Column(CHAR(36), ForeignKey('notifications.id'))
    timestamp = Column(DateTime, default=datetime.datetime.now)
    image_type = Column(String(255))
    unit_details_id = Column(CHAR(36), ForeignKey('unit_description.id'))
    club_id = Column(CHAR(36), ForeignKey('club.id'))
    field_id = Column(CHAR(36), ForeignKey('field.id'))
    user_card_id = Column(CHAR(36), ForeignKey('user_cards.id'))
    news_id = Column(CHAR(36), ForeignKey('news.id'))

    def __init__(self, **kwargs):
        super(Image, self).__init__(**kwargs)
    
    def to_json(self):

        return{
            "id": self.id,
            'path': self.path,
            'image_type': self.image_type,
            "image": "https://{}{}{}".format(BASE_URL, IMAGE_RETRIEVAL_URL, self.id)

        }