from django.contrib import admin
from .models import StoreItem

@admin.register(StoreItem)
class StoreItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'cost')
    search_fields = ('name', 'description',)
    list_filter = ('cost',)
