from django.urls import path
from . import views

urlpatterns = [
    # other URLs
    path('settings/', views.settings, name='settings'),
    path('login/', views.login, name='login'),
]