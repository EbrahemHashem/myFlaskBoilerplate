from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, ForeignKey, String, Column
from sqlalchemy.orm import backref
import datetime


import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import relationship


class Villages(Model):
    __tablename__ = 'villages'

    """ Villages model for adding new villages """

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    name = Column(String(64))
    units = relationship("Units", backref=backref("village"))
    configurations = relationship("AccessConfiguration", backref=backref("village"))
    gates = relationship("Gates", backref=backref("village"))
    buildings = relationship("Buildings", backref=backref("village"))
    project_id = Column(CHAR(36), ForeignKey('projects.id'))
    timestamp = Column(db.DateTime, default=datetime.datetime.now)
    ext_id = Column(String(64))

    def __init__(self, **kwargs):
        super(Villages, self).__init__(**kwargs)

    def to_json(self):

        return{
            "id": self.id,
            "name": self.name,
        }
   