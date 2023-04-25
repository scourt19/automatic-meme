from django.shortcuts import render
from django.core import serializers
from django.shortcuts import get_object_or_404
from event.models import Event, Location
from leaderboard.models import Leaderboard
from logins.models import Player
import json


def home(request):
    if request.user.is_authenticated:
        # Get the player object associated with the logged-in user
        player, created = Player.objects.get_or_create(user=request.user)  # Update this line
        if created:
            print(f"Created new player for user {request.user}")
        points = player.points

        events = Event.objects.values(
            'eventId', 'startDateTime', 'endDateTime', 'status',
            'trashId__name', 'locationId__buildingName',
            'locationId__latitude', 'locationId__longitude',
            'locationId__radius', 'locationId__qrCode'
        )
        events_list = list(events)
        for event in events_list:
            event['locationId__latitude'] = float(event['locationId__latitude'])
            event['locationId__longitude'] = float(event['locationId__longitude'])
            event['locationId__radius'] = float(event['locationId__radius'])
            event['startDateTime'] = event['startDateTime'].isoformat()
            event['endDateTime'] = event['endDateTime'].isoformat()
        events_json = json.dumps(events_list)
        context = {
            'events': events_json,
            'points': points
        }
        print(context)
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')



def quiz(request, event_id):
    event = get_object_or_404(Event, eventId=event_id)
    questions = event.questionSet.all()
    context = {
        'event': event,
        'questions': questions,
    }
    return render(request, 'quiz.html', context)


def resources(request):
    username = request.user.username
    return render(request, 'resources.html', {'username': username})

def settings(request):
    username = request.user.username
    return render(request, 'settings.html', {'username': username})

def store(request):
    username = request.user.username
    return render(request, 'store.html', {'username': username})

def leaderboard(request):
    Leaderboard.update_leaderboard()
    leaderboard_items = Leaderboard.objects.all()
    print("Hi " + str(leaderboard_items))  # Add this line
    return render(request, 'leaderboard.html', {'leaderboard_items': leaderboard_items})