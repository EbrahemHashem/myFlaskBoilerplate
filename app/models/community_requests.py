# from app import db
# import datetime
# from sqlalchemy.dialects.mysql import LONGBLOB

# from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, Integer, String, Column, ForeignKey
# from sqlalchemy.orm import backref, relationship
# import os

# BASE_URL = str(os.environ.get("BASE_URL"))
# IMAGE_RETRIEVAL_URL = str(os.environ.get("IMAGE_RETRIEVAL_URL"))

# import uuid
# Column = Column
# Model = db.Model

# import uuid
# from sqlalchemy.dialects.postgresql import id # idfield for PostgreSQL (or other UUID-compatible DBs)

# class Community_Request(Model):
#     __tablename__ = "community_request"
#     id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)        
    # id = Column(Integer, primary_key=True, autoincrement=True)
#     title = Column(String(255))
#     instructions = Column(db.Text, nullable=True)
#     has_attachment = Column(db.Boolean, default=False)
#     has_voice = Column(db.Boolean, default=False)
#     unit_related = Column(db.Boolean, default=False)
#     timestamp = Column(db.DateTime, default=datetime.datetime.now)

#     media = relationship('Image', backref='request', lazy='dynamic')
#     requests = relationship('Request', backref='community_request', lazy='dynamic')
    
#     __table_args__ = (
    #     Index('ix_cards_uuid', 'uuid'),  # Add an index to the idcolumn
    # )
    # def __init__(self, **kwargs):
#         super(Community_Request, self).__init__(**kwargs)

#     def to_json(self):
#         return {
#             "id": self.id,
#             "title": self.title,
#             "instructions": self.instructions,
#             "has_attachment": self.has_attachment,
#             "has_voice": self.has_voice,
#             "image": "https://{}{}{}".format(BASE_URL, IMAGE_RETRIEVAL_URL, self.images[0].id) if len(self.images)>0 else '',
#             "timestamp": str(self.timestamp)
#         }
    
#     def to_list(self):
#         return {
#             "id": self.id,
#             "title": self.title,
#             "image": "https://{}{}{}".format(BASE_URL, IMAGE_RETRIEVAL_URL, self.images[0].id) if len(self.images)>0 else '',
#         }
    
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
    
