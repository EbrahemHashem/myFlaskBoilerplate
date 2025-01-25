import datetime
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME

from app import db

import uuid
Column = Column
Model = db.Model
relationship = db.relationship

block_gates = db.Table('block_gates',
    Column('time_stamp', DATETIME, default=datetime.datetime.now),
    Column('gate_id', CHAR(36), ForeignKey("gates.id"), primary_key=True),
    Column('block_id', CHAR(36), ForeignKey("blocks.id"), primary_key=True)
    )