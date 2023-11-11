from app.extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String
from typing import List

class Aule(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(7))
    
    user: Mapped['User'] = mapped_column(db.relationship(backref='aules', lazy=True))
    students: Mapped[List['Student']] = mapped_column(db.relationship(backref='aule', lazy=True))