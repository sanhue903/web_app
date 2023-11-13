from typing import List
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String

from app.extensions import db

class User(db.Model):
    id:         Mapped[int] = mapped_column(primary_key=True)
    username:   Mapped[str] = mapped_column(db.String(20))
    email:      Mapped[str] = mapped_column(db.String(40), unique=True)
    first_name: Mapped[str] = mapped_column(db.String(20))
    last_name:  Mapped[str] = mapped_column(db.String(20))
    #password
    
    aules: Mapped[List['Aule']] = db.relationship(backref='user', lazy=True)
    
    def __init__(self, username, email, first_name, last_name):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        
    def __repr__(self):
        return f'<User {self.username}: {self.first_name} {self.last_name}>'
    
    def serialize(self):
        return {
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name
        }