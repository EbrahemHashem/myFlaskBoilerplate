from app import db
from datetime import datetime
from sqlalchemy.dialects.mysql import LONGBLOB

from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, ForeignKey
from sqlalchemy.orm import backref, relationship

import uuid
Column = Column
Model = db.Model

class News(Model):
    __tablename__ = "news"
    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        

    title = Column(String(255))
    content = Column(String(255))
    media = relationship('Image', backref='blog', lazy='dynamic')
    joined_date = Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, **kwargs):
        super(News, self).__init__(**kwargs)

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "steps": self.steps,
            "media": [med.to_json() for med in self.media],
            "joined_date": str(self.joined_date)
        }
    def to_list(self):
        return {
            "id": self.id,
            "title": self.title,
            "media": [med.to_json() for med in self.media],
            "joined_date": str(self.joined_date)
        }
