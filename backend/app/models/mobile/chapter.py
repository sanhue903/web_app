from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.extensions import db

class Chapter(db.Model):
    id: Mapped[str] = mapped_column(db.String(6), primary_key=True)
    name: Mapped[str] = mapped_column(db.String(20))
    app_mobile_id: Mapped[str] = mapped_column(db.String(6), ForeignKey('mobile_app.id'))
    
    questions: Mapped[List['Question']] = db.relationship(backref='chapters', lazy=True)
    
    def __init__(self, id, name, app_mobile_id):
        self.id = id
        self.name = name
        self.app_mobile_id = app_mobile_id
        
    def __repr__(self):
        return f'<Chapter {self.id}: {self.name}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'app_mobile_id': self.app_mobile_id
        }