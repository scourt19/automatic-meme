import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from logins.models import Player
from event.models import Trash, Event, Question
from location.models import Location
from django.utils import timezone


@pytest.mark.django_db
def test_quiz_view(client, user):
    start = timezone.now()
    end = start + timezone.timedelta(hours=2)
    player = Player.objects.create(user=user)
    client.login(username='testuser', password='testpassword')

    trash = Trash.objects.create(
        name='trash',
        description='trash description',
        value=10,
        image='website/events/image.jpg'
    )
    location = Location.objects.create(buildingName='location', latitude=0.0, longitude=0.0, radius=0.0)
    event = Event.objects.create(trashId=trash, locationId=location, status='active', startDateTime=start, endDateTime=end)
    question = Question.objects.create(question='question', answer='answer', wrongAnswer1='wrong1', wrongAnswer2='wrong2', wrongAnswer3='wrong3', wrongAnswer4='wrong4')
    event.questionSet.add(question)

    url = reverse('quiz', kwargs={'event_id': event.eventId})
    response = client.get(url)

    assert response.status_code == 200
    assert b'Trash:' in response.content
    assert b'Points:' in response.content
    assert b'Location:' in response.content
    assert b'End date:' in response.content