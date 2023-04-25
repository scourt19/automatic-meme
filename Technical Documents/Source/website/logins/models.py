from django.db import models
from django.contrib.auth.models import User, Group
from event.models import Trash, Event
from bin.models import Bin
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class PlayerGroup(Group):
    """Group authentication allowing player actions
    WARNING NOT IMPLEMENTED"""
    name = 'players'
    permissions = []

    def __str__(self):
        return self.name

class Player(models.Model):
    """Player user profile bound to one and only one User instance."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='player')
    points = models.IntegerField(default=0)
    storeItems = models.ManyToManyField('store.StoreItem')
    memberSince = models.DateTimeField(auto_now_add=True)
    attempted_events = models.ManyToManyField(Event, related_name='players_attempted')

    def __str__(self):
        return self.user.__str__()

    def add_trash_item(self, trash_item):
        bin_item, created = self.bin.binitemthrough_set.get_or_create(trash=trash_item)
        bin_item.amount += 1
        bin_item.save()

    def add_points(self, points):
        self.points += points
        self.save()

@receiver(post_save, sender=Player)
def create_bin(sender, instance, created, **kwargs):
    if created:
        Bin.objects.create(player=instance)
