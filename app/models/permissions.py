import datetime
from app import db, bcrypt
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME


# Alias common DB names
import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import relationship


class Permissions(Model):
    """ Permissions model for adding new permissions """

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    edit = Column(BOOLEAN, default=False, index=True)
    view = Column(BOOLEAN, default=False, index=True)
    add = Column(BOOLEAN, default=False, index=True)
    delete = Column(BOOLEAN, default=False, index=True)
    name = Column(String(255))
    path = Column(String(255))

    def __init__(self, **kwargs):
        super(Permissions, self).__init__(**kwargs)

