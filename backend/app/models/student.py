from app.extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String


class Student(db.Model):
    id:          Mapped[int] = mapped_column(primary_key=True)
    first_name:  Mapped[str] = mapped_column(String(15))
    last_name:   Mapped[str] = mapped_column(String(15))
    last_name_2: Mapped[str] = mapped_column(String(15))
    age:         Mapped[int]
    
    def __init__(self, first_name, last_name, last_name_2, age):
        self.first_name = first_name
        self.last_name = last_name
        self.last_name_2 = last_name_2
        self.age = age
        
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