from django.db import models
from event.models import Trash

class Bin(models.Model):
    """
    Bin model represents the player's bin containing trash items.

    Attributes:
        player (OneToOneField): The player owning the bin.
        inventory (ManyToManyField): The trash items within the bin, using the BinItemThrough model as the through model.
    """
    player = models.OneToOneField('logins.Player', on_delete=models.CASCADE, primary_key=True, related_name='bin')
    inventory = models.ManyToManyField(Trash, through='BinItemThrough', related_name='bins')

    def total_bin_value(self):
        """
        Calculate the total value of all trash items in the bin.

        Returns:
            int: Total value of all trash items in the bin.
        """
        total_value = 0
        for item in self.binitemthrough_set.all():
            total_value += item.total_value()
        return total_value

class BinItemThrough(models.Model):
    """
    BinItemThrough model represents the relationship between the Bin and Trash models.

    Attributes:
        bin (ForeignKey): Bin that the item is associated with, links to the Bin model.
        trash (ForeignKey): Trash type, links to the Trash model.
        amount (IntegerField): Quantity of the trash item in the bin.
    """
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
    trash = models.ForeignKey(Trash, on_delete=models.PROTECT)
    amount = models.IntegerField(default=0)

    def total_value(self):
        """
        Calculate the total value of the trash item in the bin.

        Returns:
            int: Total value of the trash item.
        """
        return self.trash.value * self.amount
