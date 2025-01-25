from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, ForeignKey, String, Column
from sqlalchemy.orm import backref
import datetime


import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import relationship


class GateQuota(Model):
    __tablename__ = 'gate_quota'

    """ Building model for adding new buildings """

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    unit_id = Column(CHAR(36), ForeignKey('units.id'))
    quota = Column(Integer)
    timestamp = Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, **kwargs):
        super(GateQuota, self).__init__(**kwargs)