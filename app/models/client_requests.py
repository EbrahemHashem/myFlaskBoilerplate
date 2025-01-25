from app import db
from sqlalchemy import  CHAR, ForeignKey, String

Column = db.Column
Model = db.Model
relationship = db.relationship




ClientRequests = db.Table("clientrequests",
                        #   Model.metadata,
                          Column('client_id',CHAR(36),ForeignKey("clients.id"), primary_key=True),
                          Column('request_id',String(36),ForeignKey("request.id"), primary_key=True),)


