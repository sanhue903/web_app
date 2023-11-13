from typing import List
from sqlalchemy.orm import Mapped, mapped_column

from app.extensions import db


class School(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(50))
    communes: Mapped[str] = mapped_column(db.String(50))
    region: Mapped[str] = mapped_column(db.String(50))
    
    aules: Mapped[List['Aule']] = db.relationship(backref='school', lazy=True)
    
    def __init__(self, name, communes, region):
        self.name = name
        self.communes = communes
        self.region = region
        
    def __repr__(self):
        return f'<School {self.id}: {self.name}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'communes': self.communes,
            'region': self.region
        }
        
        