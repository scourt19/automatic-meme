from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('redeem/<int:item_id>/', views.redeem_item, name='redeem_item'),
]