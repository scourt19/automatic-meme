from django.test import TestCase, Client
from django.contrib.auth.models import User
from logins.models import Player
from event.models import Trash
from bin.models import Bin, BinItemThrough
from django.utils import timezone
import random
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import MagicMock, patch


class FrontendTests(TestCase):
    """
    Test class for the frontend views of the bin app.
    """

    def setUp(self):
        """
        Set up test data for frontend tests.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def tearDown(self):
        """
        Clean up test data after running frontend tests.
        """
        self.user.delete()

    def test_player_inventory_view_not_authenticated(self):
        """
        Test the player inventory view when the user is not authenticated.

        Ensure the user is redirected to the login page when they are not authenticated.
        """
        response = self.client.get('/bin/')
        self.assertRedirects(response, '/login/?next=/bin/')

    def test_player_inventory_view_authenticated(self):
        """
        Test the player inventory view when the user is authenticated.

        Ensure the view loads the correct template and has the expected status code when the user is authenticated.
        """
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        with patch("django.core.files.uploadedfile.SimpleUploadedFile") as mock_uploaded_file:
            mock_uploaded_file.return_value = MagicMock(spec=SimpleUploadedFile)

            test_image = SimpleUploadedFile(
                name="test_image.jpg",
                content=open("bin/image.jpg", "rb").read(),
                content_type="image/jpeg"
            )

            # Create related Player and Trash instances
            player = Player.objects.create(user=self.user, points=random.randint(50, 200), memberSince=timezone.now())
            trash = Trash.objects.create(name='Plastic Bottle', value=random.randint(1, 10), image=test_image)

            # Create a Bin instance and a BinItemThrough instance
            bin = Bin.objects.create(player=player)
            bin_item = BinItemThrough.objects.create(bin=bin, trash=trash, amount=random.randint(1, 10))

            response = self.client.get('/bin/')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'bin/player_bin.html')

            # Clean up created instances
            bin.delete()
            bin_item.delete()
            trash.delete()
            player.delete()