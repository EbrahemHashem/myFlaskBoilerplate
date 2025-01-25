
import datetime
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, ForeignKey, Column, DATETIME

from sqlalchemy.orm import backref
from app import db

import uuid
Column = Column
Model = db.Model
relationship = db.relationship

EventHost = db.Table('event_host',
    Column('time_stamp', DATETIME, default=datetime.datetime.now),
    Column('event_id', CHAR(36), ForeignKey("event.id"), primary_key=True),
    Column('host_id', CHAR(36), ForeignKey("host.id"), primary_key=True)
    )
