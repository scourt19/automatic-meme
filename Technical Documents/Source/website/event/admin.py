from django.contrib import admin
from .models import Trash, Event, Question

@admin.register(Trash)
class TrashAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'description')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('eventId', 'trashId', 'locationId', 'status', 'startDateTime', 'endDateTime')
    filter_horizontal = ('questionSet',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('questionId', 'question', 'answer', 'wrongAnswer1', 'wrongAnswer2', 'wrongAnswer3', 'wrongAnswer4')
