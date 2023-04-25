from django.db import models
from django.apps import apps

class StoreItem(models.Model):
    itemId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.IntegerField()
    image = models.ImageField(upload_to='images/store_icons')
    owners = models.ManyToManyField('logins.Player', through='store.PlayerStoreItem')

    def __str__(self):
        return self.name

class PlayerStoreItem(models.Model):
    player = models.ForeignKey('logins.Player', on_delete=models.CASCADE)
    store_item = models.ForeignKey(StoreItem, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('player', 'store_item')
