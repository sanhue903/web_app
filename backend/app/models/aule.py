from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.extensions import db

class Aule(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(db.String(7))
    
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    school_id: Mapped[int] = mapped_column(ForeignKey('school.id'))
    
    students: Mapped[List['Student']] = db.relationship(backref='aule', lazy=True)
    
    def __init__(self, code, user_id, school_id):
        self.code = code
        self.user_id = user_id
        self.school_id = school_id
    
    def __repr__(self):
        return f'<Aule {self.id}: {self.code}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'code': self.code,
            'user_id': self.user_id,
            'school_id': self.school_id
        }
        