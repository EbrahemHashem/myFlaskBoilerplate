from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, ForeignKey
import datetime

import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import backref, relationship

class BlackList(Model):
    __tablename__ = 'blacklist'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    gate_id = Column(CHAR(36), ForeignKey('gates.id'))
    client_id = Column(CHAR(36), ForeignKey('clients.id'))
    timestamp = Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, **kwargs):
        super(BlackList, self).__init__(**kwargs)

    def to_json(self):

        return {
            "id": self.id,
            "name": self.name
            }