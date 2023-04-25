import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from logins.models import Player
from django.test import Client


# Fixture to create a test user
@pytest.fixture
def user():
    """Create a test user and return it."""
    return User.objects.create_user(username='testuser', password='testpassword')


# Fixture to create a client with a logged-in user
@pytest.fixture
def client_with_logged_in_user():
    """
    Create a test user, associate it with a Player, log in the user,
    and return the logged-in client.
    """
    user = User.objects.create_user(username='testuser', password='testpassword')
    Player.objects.create(user=user)
    client = Client()
    client.login(username='testuser', password='testpassword')
    return client


# Test to check if the quiz template is rendered correctly
@pytest.mark.django_db
def test_quiz_template(client_with_logged_in_user, event):
    """
    Test if the 'logins/base_loggedin_back.html' template is used when accessing
    the quiz page with a logged-in user.
    """
    response = client_with_logged_in_user.get(
        reverse('quiz', kwargs={'event_id': event.eventId})
    )
    assert 'logins/base_loggedin_back.html' in [t.name for t in response.templates]