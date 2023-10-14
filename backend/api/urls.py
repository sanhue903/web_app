from django.urls import path

from . import views

urlpatterns = [
    path('student/get', views.get_student, name='student'),
]
