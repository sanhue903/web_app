from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from typing import List

from app.extensions import db


class Student(db.Model):
    id:          Mapped[int] = mapped_column(primary_key=True)
    first_name:  Mapped[str] = mapped_column(db.String(15))
    last_name:   Mapped[str] = mapped_column(db.String(15))
    last_name_2: Mapped[str] = mapped_column(db.String(15))
    age:         Mapped[int]
    
    aule_id: Mapped[int] = mapped_column(ForeignKey('aule.id'))
    mobile_app_id: Mapped[str] = mapped_column(db.String(6))
    
    scores: Mapped[List['Score']] = db.relationship(backref='student', lazy=True)    
    
    def __init__(self, first_name, last_name, last_name_2, age, aule_id, mobile_app_id):
        self.first_name = first_name
        self.last_name = last_name
        self.last_name_2 = last_name_2
        self.age = age
        self.aule_id = aule_id
        self.mobile_app_id = mobile_app_id
        
    def __repr__(self):
        return f'<Student {self.id}: {self.first_name} {self.last_name}>'
        
    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'last_name_2': self.last_name_2,
            'age': self.age
        }