# from app import db
# import datetime
# from sqlalchemy.dialects.mysql import LONGBLOB

# from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, Integer, String, Column, ForeignKey
# from sqlalchemy.orm import backref, relationship

# import uuid
# Column = Column
# Model = db.Model

# import uuid
# from sqlalchemy.dialects.postgresql import id # idfield for PostgreSQL (or other UUID-compatible DBs)

# class Request(Model):
#     __tablename__ = "request"
#     id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # # old_id = Column(Integer)        
    # id = Column(Integer)
    # id = Column(Integer, primary_key=True, autoincrement=True)
#     title = Column(String(255))
#     instructions = Column(db.Text, nullable=True)
#     has_attachment = Column(db.Boolean, default=False)
#     has_voice = Column(db.Boolean, default=False)
#     unit_related = Column(db.Boolean, default=False)
#     timestamp = Column(db.DateTime, default=datetime.datetime.now)
#     request_id = Column(CHAR(36), ForeignKey('community_request.id'))
#     client_id = Column(CHAR(36), ForeignKey('clients.id'))
#     unit_id = Column(CHAR(36), ForeignKey('units.id'))
    
#     media = relationship('Image', backref='request', lazy='dynamic')
    
#     __table_args__ = (
    #     Index('ix_cards_uuid', 'uuid'),  # Add an index to the idcolumn
    # )
    # def __init__(self, **kwargs):
#         super(Request, self).__init__(**kwargs)

#     def to_json(self):
#         return {
#             "id": self.id,
#             "title": self.title,
#             "instructions": self.instructions,
#             "has_attachment": self.has_attachment,
#             "has_voice": self.has_voice,
#             "media": [med.to_json() for med in self.media],
#             "timestamp": str(self.timestamp)
#         }
    
