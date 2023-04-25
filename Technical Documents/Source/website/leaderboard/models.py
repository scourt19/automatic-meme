from django.db import models
from django.contrib.auth.models import User
from bin.models import Bin
import logins.models


class Leaderboard(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    total_value = models.IntegerField(default=0)

    class Meta:
        ordering = ['-total_value']

    def __str__(self):
        return f"{self.player.username}'s total value: {self.total_value}"

    @classmethod
    def update_leaderboard(self):
        leaderboard_items = Leaderboard.objects.all()
        for item in leaderboard_items:
            try:
                item.total_value = item.player.player.bin.total_bin_value()
                item.save()
            except logins.models.Player.bin.RelatedObjectDoesNotExist:
                # Handle the case where the Player object does not have a related Bin object
                item.total_value = 0
                item.save()


    @classmethod
    def create_leaderboard(cls):
        print("Creating leaderboard")
        players = User.objects.filter(groups__name='players')

        for player in players:
            cls.objects.create(player=player)