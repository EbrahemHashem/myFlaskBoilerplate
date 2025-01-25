from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, ForeignKey, Column, DATETIME
import datetime
from app import db

import uuid
Column = Column
Model = db.Model
relationship = db.relationship


RolesPermissions = db.Table('roles_permissions',
    Column('time_stamp', DATETIME, default=datetime.datetime.now),
    Column('role_id', CHAR(36), ForeignKey("roles.id"), primary_key=True),
    Column('permission_id', CHAR(36), ForeignKey("permissions.id"), primary_key=True)
    )
