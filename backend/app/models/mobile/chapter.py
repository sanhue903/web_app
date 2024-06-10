from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.extensions import db

class Chapter(db.Model):
    id: Mapped[str] = mapped_column(db.String(6), primary_key=True)
    name: Mapped[str] = mapped_column(db.String(20))
    number: Mapped[int] 

    app_id: Mapped[str] = mapped_column(db.String(6), ForeignKey('application.id'))
    
    questions: Mapped[List['Question']] = db.relationship(backref='chapter', lazy=True)
    
    def __init__(self, id, number, name, app_id):
        self.id = id
        self.number = number
        self.name = name
        self.app_id = app_id
        
    def __repr__(self):
        return f'<Chapter {self.id}: {self.name}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'app_id': self.app_id
        }