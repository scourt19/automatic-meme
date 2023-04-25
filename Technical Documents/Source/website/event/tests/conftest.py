from event.models import Event, Trash
from location.models import Location
from django.utils import timezone
import pytest
from django.contrib.auth.models import User

@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='testpassword')

@pytest.fixture
def event():
    start = timezone.now() + timezone.timedelta(days=1)
    end = start + timezone.timedelta(hours=2)
    trash = Trash.objects.create(name='trash', description='trash description', value=10)
    location = Location.objects.create(buildingName='location', latitude=0.0, longitude=0.0, radius=0.0)
    return Event.objects.create(
        trashId=trash,
        locationId=location,
        status='active',
        startDateTime=start,
        endDateTime=end
    )