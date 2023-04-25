import pytest
from django.db import IntegrityError
from django.contrib.auth.models import User
from logins.models import Player
from event.models import Trash
from bin.models import Bin, BinItemThrough
from django.utils import timezone
from django.db import transaction


@pytest.fixture
def test_data():
    # Create test user, player, and trash instances for testing
    user = User.objects.create_user(username='testuser', password='testpassword')
    player = Player.objects.create(user=user, points=100, memberSince=timezone.now())
    trash = Trash.objects.create(name='Plastic Bottle', value=5)
    return user, player, trash


@pytest.mark.django_db
def test_unique_player_bin(test_data):
    """
    Test to ensure a player can have only one bin.
    Each player should have a unique bin associated with them.
    """
    user, player, _ = test_data

    # Create the first bin for the player
    bin1 = Bin.objects.create(player=player)

    # Attempt to create a second bin for the same player, expect IntegrityError
    # An IntegrityError should be raised since each player can have only one bin
    with transaction.atomic():
        with pytest.raises(IntegrityError):
            bin2 = Bin.objects.create(player=player)

    # Clean up by deleting the created bin
    bin1.delete()


@pytest.mark.django_db
def test_bin_item_delete_with_bin(test_data):
    """
    Test to ensure that BinItemThrough instances are deleted when the associated bin is deleted.
    When a bin is deleted, all related BinItemThrough instances should also be removed.
    """
    _, player, trash = test_data

    # Create a bin for the player
    bin = Bin.objects.create(player=player)
    # Create a BinItemThrough instance that associates the bin and trash
    bin_item = BinItemThrough.objects.create(bin=bin, trash=trash, amount=1)

    # Store the primary keys of the bin and bin_item for later reference
    bin_id = bin.pk
    bin_item_id = bin_item.pk

    # Delete the bin, which should also delete associated BinItemThrough instances
    bin.delete()

    # Check if the bin and bin_item instances have been deleted
    # Both the Bin and BinItemThrough instances should no longer exist in the database
    assert not Bin.objects.filter(pk=bin_id).exists()
    assert not BinItemThrough.objects.filter(pk=bin_item_id).exists()
