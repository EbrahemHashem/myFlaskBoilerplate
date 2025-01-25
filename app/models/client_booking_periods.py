import datetime
import datetime
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, ForeignKey, Column, DATETIME

from sqlalchemy.orm import backref
from app import db

import uuid
Column = Column
Model = db.Model
relationship = db.relationship

ClientRentals = db.Table('booked_periods',
    Column('time_stamp', DATETIME, default=datetime.datetime.now),
    Column('client_id', CHAR(36), ForeignKey("clients.id"), primary_key=True),
    Column('booking_period_id', CHAR(36), ForeignKey("unitbooking.id"), primary_key=True)
    )
