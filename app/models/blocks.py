import datetime
from app import db
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, ForeignKey, DateTime
from app.models.block_gates import block_gates
from app.models.unit_blocks import unit_blocks
from datetime import datetime as date
from sqlalchemy.orm import backref

# Alias common DB names
import uuid
Column = Column
Model = db.Model
relationship = db.relationship
class Blocks(Model):
    __tablename__ = 'blocks'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    name = Column(String(255))
    gates = relationship("Gates", secondary = block_gates, backref=backref("blocks"), lazy="dynamic")
    units = relationship("Units", secondary = unit_blocks, backref=backref("blocks"), lazy="dynamic")

    created_at = Column(DateTime, default=datetime.datetime.now)

    def __init__(self, **kwargs):
        super(Blocks, self).__init__(**kwargs)
    
