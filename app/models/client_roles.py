import datetime
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, UniqueConstraint

from sqlalchemy.orm import backref
from app import db, bcrypt

import uuid
Column = Column
Model = db.Model
relationship = db.relationship


class ClientRoles(Model):

    __tablename__ = "client_roles"

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    
    village_id = Column(ForeignKey("villages.id"), primary_key=True)
    client_id = Column(ForeignKey("clients.id"), primary_key=True)
    role_id = Column(ForeignKey("roles.id"), nullable=False)
    timestamp = Column(db.DateTime, default=datetime.datetime.now)

    __table_args__ = (UniqueConstraint(client_id, village_id, role_id),)

    client = relationship("Client", backref = backref("client_roles"))
    role = relationship("Role", backref = backref("client_roles"))
    village = relationship("Villages", backref = backref("client_roles"))