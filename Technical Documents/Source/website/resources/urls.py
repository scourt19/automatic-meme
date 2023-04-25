from django.urls import path
from . import views

urlpatterns = [
    # other URLs
    path('resources/', views.resources, name='resources'),
]