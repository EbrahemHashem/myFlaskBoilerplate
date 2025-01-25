from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, ForeignKey
import datetime

import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import backref, relationship

class Host(db.Model):
    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        

    name = Column(db.String(120))
    phone = Column(db.String(20))
    email = Column(db.String(120))
    timestamp = Column(db.DateTime, default=datetime.datetime.now)


    def _init_(self, **kwargs):
        super(Host, self)._init_(**kwargs)
        
    def to_json(self):

        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email
            }