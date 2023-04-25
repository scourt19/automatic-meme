from django.db import models
import decimal

class Location(models.Model):
    locationId = models.AutoField(primary_key=True)
    buildingName = models.CharField(max_length=100)
    qrCode = models.CharField(max_length=50)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=decimal.Decimal('0.0'))
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=decimal.Decimal('0.0'))
    radius = models.DecimalField(max_digits=5, decimal_places=2, default=decimal.Decimal('0.0'))

    def __str__(self) -> str:
        return self.buildingName