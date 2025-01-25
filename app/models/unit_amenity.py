from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, ForeignKey, Column, DATETIME
import datetime
from app import db

import uuid
Column = Column
Model = db.Model
relationship = db.relationship


UnitAmenities = db.Table('unit_amenity',
    Column('time_stamp', DATETIME, default=datetime.datetime.now),
    Column('unit_id', CHAR(36), ForeignKey("units.id"), primary_key=True),
    Column('amenity_id', CHAR(36), ForeignKey("amenity.id"), primary_key=True)
    )
