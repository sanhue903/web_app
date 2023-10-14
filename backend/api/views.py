from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mobile.models import *
from mobile.serializers import *
# Create your views here.

@api_view(['GET'])
def get_student(request):
    instance = Student.objects.all().first()
    
    data = {}
    if instance:
        data = StudentSerializer(instance).data
    return Response(data)
