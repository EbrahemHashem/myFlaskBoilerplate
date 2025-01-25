from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, ForeignKey, String, Column
from sqlalchemy.orm import backref
import datetime


import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import relationship


class Buildings(Model):
    __tablename__ = 'buildings'

    """ Building model for adding new buildings """

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    name = Column(String(64))
    units = relationship("Units", backref=backref("building"))
    village_id = Column(CHAR(36), ForeignKey('villages.id'))
    timestamp = Column(db.DateTime, default=datetime.datetime.now)
    ext_id = Column(String(64))
    gates = relationship("Gates", backref=backref("building"), uselist= False)

    def __init__(self, **kwargs):
        super(Buildings, self).__init__(**kwargs)