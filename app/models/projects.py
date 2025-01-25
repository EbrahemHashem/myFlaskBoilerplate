from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, ForeignKey, String, Column
from sqlalchemy.orm import backref
import datetime


import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import relationship

class Projects(Model):
    __tablename__ = 'projects'

    """ Projects model for adding new projects """

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    name = Column(String(255))
    villages = relationship("Villages", backref=backref("project"))
    utilities = relationship("Utilities", backref=backref("project"))
    developer_id = Column(CHAR(36), ForeignKey('developers.id'))
    ext_id = Column(String(64))
    timestamp = Column(db.DateTime, default=datetime.datetime.now)


    def __init__(self, **kwargs):
        super(Projects, self).__init__(**kwargs)