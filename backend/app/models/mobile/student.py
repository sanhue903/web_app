from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from typing import List

from app.extensions import db


class Student(db.Model):
    id:   Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(50))
    age:  Mapped[int]
    
    aule_id: Mapped[int] = mapped_column(ForeignKey('aule.id'))
    mobile_app_id: Mapped[str] = mapped_column(db.String(6))
    
    scores: Mapped[List['Score']] = db.relationship(backref='student', lazy=True)    
    
    def __init__(self, name, age, aule_id, mobile_app_id):
        self.name = name    
        self.age = age
        self.aule_id = aule_id
        self.mobile_app_id = mobile_app_id
        
    def __repr__(self):
        return f'<Student {self.id}: {self.name}>'
        