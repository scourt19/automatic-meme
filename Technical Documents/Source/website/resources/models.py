from django.db import models

class Resource(models.Model):
    resourceId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self) -> str:
        return self.title