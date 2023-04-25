import pytest
import random
from django.contrib.auth.models import User
from logins.models import Player
from event.models import Trash
from bin.models import Bin, BinItemThrough
from django.utils import timezone
from bin.views import player_inventory
from django.http import HttpRequest
from django.test import RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import MagicMock, patch
from django.core.files import File

# Fixture for test data
@pytest.fixture
def test_data():
    """
    Fixture to create test data for tests, including User, Player, and Trash instances.

    Returns:
        tuple: A tuple containing User, Player, and Trash instances.
    """
    # Image placeholder
    with patch("django.core.files.uploadedfile.SimpleUploadedFile") as mock_uploaded_file, \
            patch("django.core.files.File") as mock_file:
        mock_uploaded_file.return_value = MagicMock(spec=SimpleUploadedFile)
        mock_file.return_value = MagicMock(spec=File)

        test_image = SimpleUploadedFile(
            name="test_image.jpg",
            content=open("bin/image.jpg", "rb").read(),
            content_type="image/jpeg"
        )

        # Create related Player and Trash instances
        user = User.objects.create_user(username='testuser', password='testpassword')
        player = Player.objects.create(user=user, points=random.randint(50, 200), memberSince=timezone.now())
        trash = Trash.objects.create(name='Plastic Bottle', value=random.randint(1, 10), image=test_image)

        yield user, player, trash

        user.delete()
        player.delete()
        trash.delete()

# Test BinItemThrough model
@pytest.mark.django_db
def test_bin_item(test_data):
    """
    Test the BinItemThrough model and its total_value method.
    """
    _, player, trash = test_data

    # Create a bin for the player and a BinItemThrough instance
    player_bin = Bin.objects.create(player=player)
    bin_item = BinItemThrough.objects.create(bin=player_bin, trash=trash, amount=random.randint(1, 10))

    assert bin_item.trash == trash
    assert bin_item.total_value() == trash.value * bin_item.amount

    bin_item.delete()
    player_bin.delete()

# Test Bin model
@pytest.mark.django_db
def test_bin(test_data):
    """
    Test the Bin model and its total_bin_value method.
    """
    _, player, trash = test_data

    # Create a bin for the player and a BinItemThrough instance
    bin = Bin.objects.create(player=player)
    bin_item = BinItemThrough.objects.create(bin=bin, trash=trash, amount=random.randint(1, 10))

    assert bin.player == player
    assert bin.inventory.count() == 1
    assert bin.total_bin_value() == bin_item.total_value()

    bin_item.delete()
    bin.delete()

# Test player_inventory view
@pytest.mark.django_db
def test_player_inventory_view(test_data):
    """
    Test the player_inventory view to ensure it displays the correct context data.
    """
    user, player, trash = test_data
    factory = RequestFactory()
    request = factory.get('/bin/player_inventory/')
    request.user = user

    # Create a bin for the player and a BinItemThrough instance
    player_bin = Bin.objects.create(player=player)
    bin_item = BinItemThrough.objects.create(bin=player_bin, trash=trash, amount=random.randint(1, 10))

    response = player_inventory(request)

    assert response