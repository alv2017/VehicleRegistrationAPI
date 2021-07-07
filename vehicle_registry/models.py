import re
from django.db import models
from django.core.exceptions import ValidationError


def validate_number(number):
    pattern = r'^[a-z]{3}\d{3}$'
    if not re.match(pattern, number, re.I):
        raise ValidationError("Invalid vehicle number: {number}.")


class Vehicle(models.Model):
    number = models.CharField(max_length=6, unique=True, validators=[validate_number])
    maker = models.CharField(max_length=32)
    manufacturing_date = models.DateField()
    series = models.CharField(max_length=3, auto_created=True)
    create_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('number',)

    def __str__(self):
        return self.number

    def save(self, *args, **kwargs):
        self.series = self.number[:3]
        super().save(*args, **kwargs)





