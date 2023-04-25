from django.db import models
from location.models import Location
from django.core.exceptions import ValidationError


class Trash(models.Model):
    trashId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    value = models.IntegerField()
    image = models.ImageField(upload_to='images/trash_icons', default='image.jpg')

    def __str__(self):
        return '%s' % self.name


class Event(models.Model):
    eventId = models.AutoField(primary_key=True)
    trashId = models.ForeignKey(Trash, on_delete=models.CASCADE)
    locationId = models.ForeignKey(Location, on_delete=models.CASCADE)
    questionSet = models.ManyToManyField('Question')
    status = models.CharField(max_length=100)
    startDateTime = models.DateTimeField()
    endDateTime = models.DateTimeField()

    def __str__(self):
        return f"{self.trashId} at {self.locationId}"



class Question(models.Model):
    questionId = models.AutoField(primary_key=True)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    wrongAnswer1 = models.CharField(max_length=100)
    wrongAnswer2 = models.CharField(max_length=100)
    wrongAnswer3 = models.CharField(max_length=100)
    wrongAnswer4 = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % self.question

    def get_choices(self):
        choices = [(self.answer, self.answer),
                   (self.wrongAnswer1, self.wrongAnswer1),
                   (self.wrongAnswer2, self.wrongAnswer2),
                   (self.wrongAnswer3, self.wrongAnswer3),
                   (self.wrongAnswer4, self.wrongAnswer4)]
        return choices