from rest_framework import generics

from .models import *
from .serializers import *


class StudentCreateAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    
class ScoreListAPIView(generics.ListAPIView):    
    student = Student.objects.get(id=1)
    queryset = Score.objects.all().filter(student=student)
    serializer_class = ScoreSerializer
    
class ScoreCreateAPIView(generics.CreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer