from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, ForeignKey, Column, DATETIME
import datetime
from app import db

import uuid
Column = Column
Model = db.Model
relationship = db.relationship

UserServices = db.Table('user_requests',
    Column('time_stamp', DATETIME, default=datetime.datetime.now),
    Column('user_id', CHAR(36), ForeignKey("user.id"), primary_key=True),
    Column('order_id', CHAR(36), ForeignKey("service_order.id"), primary_key=True)
    )
