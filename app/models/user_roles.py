import datetime
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, UniqueConstraint

from sqlalchemy.orm import backref
from app import db, bcrypt

import uuid
Column = Column
Model = db.Model
relationship = db.relationship


class UserProjectRoles(Model):

    __tablename__ = "user_roles"

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    village_id = Column(ForeignKey('villages.id'), nullable=False)
    
    user_id = Column(ForeignKey('user.id'), nullable=False)
    role_id = Column(CHAR(36), ForeignKey('roles.id'), nullable=False)
    timestamp = Column(db.DateTime, default=datetime.datetime.now)

    # __table_args__ = (UniqueConstraint(user_id, village_id, role_id),)

    user = relationship("User", backref = backref("user_projects_roles"))
    role = relationship("Role", backref = backref("user_projects_roles"))
    village = relationship("Villages", backref = backref("user_projects_roles"))