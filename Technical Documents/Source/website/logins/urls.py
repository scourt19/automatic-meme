from django.urls import path, include
from django.contrib.auth.urls import views as auth_views

from . import views

app_name = 'logins'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
]
