from app.extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String
from typing import List

class User(db.Model):
    username:   Mapped[str] = mapped_column(String(20))
    email:      Mapped[str] = mapped_column(String(40), unique=True)
    first_name: Mapped[str] = mapped_column(String(20))
    last_name:  Mapped[str] = mapped_column(String(20))
    #password
    
    aules: Mapped[List['Aule']] = mapped_column(db.relationship(backref='user', lazy=True))