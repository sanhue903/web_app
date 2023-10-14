from rest_framework import generics

from .models import *
from .serializers import *

class ScoreDetailAPIView(generics.ListAPIView):
    student = Student.objects.get(id=1)
    queryset = Score.objects.all().filter(student=student)
    serializer_class = ScoreSerializer