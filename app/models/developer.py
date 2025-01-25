from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column
import datetime
from sqlalchemy import event

import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import backref, relationship

class Developer(Model):
    __tablename__ = 'developers'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    name = Column(String(64))
    project = relationship('Projects', backref=backref('developer'))
    timestamp = Column(db.DateTime, default=datetime.datetime.now)
   
    def __init__(self, **kwargs):
        super(Developer, self).__init__(**kwargs)

    def to_json(self):

        return {
            "id": self.id,
            "name": self.name,
            "project": [ {"id": a.id, "name": a.name} for a in self.project] if self.project else None
        }

@event.listens_for(Developer.__table__, 'after_create')
def create_departments(*args, **kwargs):
    db.session.add(Developer(name='Customer Service', email='abc@domain.com'))
    db.session.add(Developer(name='IT', email='def@domain.com'))
    db.session.commit()
