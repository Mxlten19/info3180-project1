from app import db
from datetime import datetime

class Property(db.Model):
    __tablename__ = 'properties'

    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title       = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    no_of_rooms = db.Column(db.Integer, nullable=False)
    no_of_baths = db.Column(db.Integer, nullable=False)
    price       = db.Column(db.Numeric(15, 2), nullable=False)
    prop_type   = db.Column(db.String(50), nullable=False)   # 'House' or 'Apartment'
    location    = db.Column(db.String(255), nullable=False)
    photo       = db.Column(db.String(255), nullable=False)
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Property {self.id}: {self.title}>'
