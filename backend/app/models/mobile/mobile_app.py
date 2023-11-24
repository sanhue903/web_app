from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.extensions import db

class MobileApp(db.Model):
    id: Mapped[str] = mapped_column(db.String(6), primary_key=True)
    name: Mapped[str] = mapped_column(db.String(50))

    aules: Mapped[List['Aule']] = db.relationship(backref='mobile_app', lazy=True)
    chapters: Mapped[List['Chapter']] = db.relationship(backref='mobile_app', lazy=True)
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def __repr__(self):
        return f'<AppMobile {self.id}: {self.name}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }