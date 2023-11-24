from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.extensions import db

class Question(db.Model):
    id: Mapped[str] = mapped_column(db.String(6), primary_key=True)
    text: Mapped[str] = mapped_column(db.String(50))
    chapter_id: Mapped[str] = mapped_column(db.String(6), ForeignKey('chapter.id'))
    
    scores: Mapped[List['Score']] = db.relationship(backref='question', lazy=True)
    
    def __init__(self, id, text, chapter_id):
        self.id = id
        self.text = text
        self.chapter_id = chapter_id
        
    def __repr__(self):
        return f'<Question {self.id}: {self.text}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'text': self.text,
            'app_mobile_id': self.app_mobile_id
        }
    