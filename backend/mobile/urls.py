from django.urls import path

from . import views

urlpatterns = [
    path('score/<int:pk>', views.ScoreListAPIView.as_view(), name='score'),
    path('score/', views.ScoreCreateAPIView.as_view(), name='add_score'),
    path('student/', views.StudentCreateAPIView.as_view(), name='student'),
]