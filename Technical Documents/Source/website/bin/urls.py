from django.urls import path
from . import views

urlpatterns = [
    path('', views.player_inventory, name='bin'),
    path('<int:trash_id>/', views.trash_detail, name='trash_detail'),
]