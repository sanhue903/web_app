from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
import datetime

from app.extensions import db

class Score(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey('student.id'))
    question_id: Mapped[str] = mapped_column(ForeignKey('question.id'))
    miliseconds: Mapped[int] 
    attempts: Mapped[int]
    
    def __init__(self, student_id, question_id, miliseconds, attempts):
        self.student_id = student_id
        self.question_id = question_id
        self.miliseconds = miliseconds
        self.attempts = attempts

    def __repr__(self):
        return f'<Score {self.id}: {self.question_id} - {self.attempts} - {self.miliseconds}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'question_id': self.question_id,
            'student_id': self.student_id,
            'time': self.miliseconds,
            'attempts': self.attempts
        }
    
    
