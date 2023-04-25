import pytest
from event.models import Trash, Event, Question
from location.models import Location
from django.utils import timezone

start_time = timezone.now()
end_time = start_time + timezone.timedelta(hours=24)

@pytest.mark.django_db
def test_trash_creation() -> None:
    """
    Test the creation of a Trash object with specific attributes.
    Verify that the attributes of the created object match the expected values.
    """
    trash = Trash.objects.create(name='trash', description='trash description', value=10)

    assert trash.name == 'trash'
    assert trash.description == 'trash description'
    assert trash.value == 10


@pytest.mark.django_db
def test_event_creation() -> None:
    """
    Test the creation of an Event object with specific attributes.
    Verify that the attributes of the created object match the expected values.
    """
    trash = Trash.objects.create(name='trash', description='trash description', value=10)
    location = Location.objects.create(buildingName='location', latitude=0.0, longitude=0.0, radius=0.0)
    event = Event.objects.create(trashId=trash, locationId=location, status='active', startDateTime=start_time, endDateTime=end_time)

    assert event.trashId == trash
    assert event.locationId == location
    assert event.status == 'active'


@pytest.mark.django_db
def test_question_creation() -> None:
    """
    Test the creation of a Question object with specific attributes.
    Verify that the attributes of the created object match the expected values.
    Additionally, test the get_choices() method to ensure it returns the correct list of choices.
    """
    question = Question.objects.create(question='question', answer='answer', wrongAnswer1='wrong1', wrongAnswer2='wrong2', wrongAnswer3='wrong3', wrongAnswer4='wrong4')

    assert question.question == 'question'
    assert question.answer == 'answer'
    assert question.wrongAnswer1 == 'wrong1'
    assert question.wrongAnswer2 == 'wrong2'
    assert question.wrongAnswer3 == 'wrong3'
    assert question.wrongAnswer4 == 'wrong4'

    choices = question.get_choices()
    assert ('answer', 'answer') in choices
    assert ('wrong1', 'wrong1') in choices
    assert ('wrong2', 'wrong2') in choices
    assert ('wrong3', 'wrong3') in choices
    assert ('wrong4', 'wrong4') in choices
