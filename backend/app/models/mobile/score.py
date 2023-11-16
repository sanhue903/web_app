from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
import datetime

from app.extensions import db

class Score(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[str] = mapped_column(ForeignKey('question.id'))
    student_id: Mapped[int] = mapped_column(ForeignKey('student.id'))
    time: Mapped[datetime.datetime] = mapped_column(db.DateTime, default=datetime.datetime.now)#revisar default
    attempts: Mapped[int] = mapped_column(db.Integer, default=1)
    
    def __init__(self, question_id, student_id, time, attempts):
        self.question_id = question_id
        self.student_id = student_id
        self.time = time
        self.attempts = attempts

    def __repr__(self):
        return f'<Score {self.id}: {self.question_id} - {self.attempts} - {self.time}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'question_id': self.question_id,
            'student_id': self.student_id,
            'time': self.time,
            'attempts': self.attempts
        }
    
    
