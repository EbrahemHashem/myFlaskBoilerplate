from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, ForeignKey
import datetime

import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import backref, relationship

class Gates(Model):
    __tablename__ = 'gates'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    name = Column(String(255))
    anpr_ip = Column(String(255))
    long_range_ip = Column(String(255))
    ip = Column(String(255))
    port = Column(String(255))
    gate_mod = Column(String(255))
    user_name = Column(String(255))
    password = Column(String(255))
    direction = Column(String(255))
    face_rec_ip = Column(String(255))
    hikvision_ip = Column(String(255))
    cctv_ip = Column(String(255))
    village_id = Column(CHAR(36), ForeignKey('villages.id'))
    unit_id = Column(CHAR(36), ForeignKey('units.id'))
    building_id = Column(CHAR(36), ForeignKey('buildings.id'))
    type_id = Column(CHAR(36), ForeignKey('types.id'))
    gate_schedules = relationship("GateSchedule", backref=backref("gate"))
    whitelisted_gates = relationship("WhiteList", backref=backref("gate"))
    blacklisted_gates = relationship("BlackList", backref=backref("gate"))

    timestamp = Column(db.DateTime, default=datetime.datetime.now)
    
    def __init__(self, **kwargs):
        super(Gates, self).__init__(**kwargs)

        
    def to_json(self):

        return {
            "id": self.id,
            "name": self.name
            }