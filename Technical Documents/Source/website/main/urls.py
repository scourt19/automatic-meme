from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('resources/', views.resources, name='resources'),
    path('settings/', views.settings, name='settings'),
    path('store/', views.store, name='store'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]