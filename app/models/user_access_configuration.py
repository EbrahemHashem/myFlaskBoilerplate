import datetime
from app import db, bcrypt
from sqlalchemy import CHAR, ForeignKey, String, Column, BOOLEAN, DateTime, DATETIME, Integer, BOOLEAN, Integer, ForeignKey, String, Column, CHAR, String, Column, BOOLEAN, ForeignKey, DATETIME
from sqlalchemy.orm import backref
# Alias common DB names
import uuid
Column = Column
Model = db.Model
from sqlalchemy.orm import relationship

class AccessConfiguration(Model):
    __tablename__ = 'card_configuration'

    id= Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False, unique=True, index=True)
    # old_id = Column(Integer)        
    maximum_extra_cards = Column(Integer)
    extra_cards_fees = Column(Integer)
    maximum_first_cards = Column(Integer)
    first_issue_fees = Column(Integer)
    reissuance_fees = Column(Integer)
    insured = Column(BOOLEAN, default=False, index=True)
    insurance_fees = Column(Integer)
    cards_per_bedroom = Column(Integer)
    expiry_date = Column(db.DateTime)
    minimum_stay = Column(Integer)
    minimum_stay_price = Column(Integer)
    timestamp = Column(db.DateTime, default=datetime.datetime.now)
    access_type_id = Column(CHAR(36), db.ForeignKey('types.id'))
    user_type_id = Column(CHAR(36), db.ForeignKey('types.id'))
    village_id = Column(CHAR(36), ForeignKey('villages.id'))

    access_type = db.relationship('Types', foreign_keys=[access_type_id], backref='access_type_config')
    user_type = db.relationship('Types', foreign_keys=[user_type_id], backref='user_access_config')

    def __init__(self, **kwargs):
        super(AccessConfiguration, self).__init__(**kwargs)
    
    def to_json(self):

        return {
            "id": self.id,
            "maximum_extra_cards": self.maximum_extra_cards,
            "extra_cards_fees": self.extra_cards_fees,
            "maximum_first_cards": self.maximum_first_cards,
            "first_issue_fees": self.first_issue_fees,
            "reissuance_fees": self.reissuance_fees,
            "insured": self.insured,
            "insurance_fees": self.insurance_fees,
            "cards_per_bedroom": self.cards_per_bedroom,
            "expiry_date": str(self.expiry_date),
            "minimum_stay": self.minimum_stay,
            "minimum_stay_price": self.minimum_stay_price,
            "timestamp": str(self.timestamp),
            "access_type": self.access_type.name,
            "user_type": self.user_type.name,
            "village": self.village.name if self.village else None,
        }