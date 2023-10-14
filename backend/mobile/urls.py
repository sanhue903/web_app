from django.urls import path

from . import views

urlpatterns = [
    path('score/<int:pk>', views.ScoreDetailAPIView.as_view(), name='score'),
]