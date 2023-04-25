from django.shortcuts import render
from .models import Leaderboard

def leaderboard(request):
    Leaderboard.update_leaderboard()
    leaderboard_items = Leaderboard.objects.all()
    print("Hi " + str(leaderboard_items))  # Add this line
    return render(request, 'leaderboard.html', {'leaderboard_items': leaderboard_items})