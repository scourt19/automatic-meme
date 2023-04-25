from django.urls import path
from . import views

urlpatterns = [
    # other URLs
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]