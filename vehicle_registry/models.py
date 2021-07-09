import re
from datetime import date
from django.db import models
from django.core.exceptions import ValidationError


def validate_number(number):
    pattern = r'^[a-z]{3}\d{3}$'
    if not re.match(pattern, number, re.I):
        raise ValidationError("Invalid vehicle number: {number}.")


def validate_manufacturing_date(manufacturing_date):
    if manufacturing_date < date(year=1920, month=1, day=1) or manufacturing_date > date.today():
        raise ValidationError("Invalid manufacturing date.")


class Vehicle(models.Model):
    MANUFACTURERS = [
        ('AC', 'AC'),
        ('Acura', 'Acura'),
        ('Aixam', 'Aixam'),
        ('Alfa Romeo', 'Alfa Romeo'),
        ('Alpina', 'Alpina'),
        ('Asia', 'Asia'),
        ('Aston Martin', 'Aston Martin'),
        ('Audi', 'Audi'),
        ('Austin Rover', 'Austin Rover'),
        ('Bentley', 'Bentley'),
        ('BMW', 'BMW'),
        ('Buick', 'Buick'),
        ('Cadillac', 'Cadillac'),
        ('Chevrolet', 'Chevrolet'),
        ('Chrysler', 'Chrysler'),
        ('Citroen', 'Citroen'),
        ('Dacia', 'Dacia'),
        ('Daewoo', 'Daewoo'),
        ('Daihatsu', 'Daihatsu'),
        ('Datsun', 'Datsun'),
        ('Dodge', 'Dodge'),
        ('Ferrari', 'Ferrari'),
        ('Fiat', 'Fiat'),
        ('Fisker', 'Fisker'),
        ('Ford', 'Ford'),
        ('GAZ', 'GAZ'),
        ('GMC', 'GMC'),
        ('Honda', 'Honda'),
        ('Hummer', 'Hummer'),
        ('Hyundai', 'Hyundai'),
        ('Infiniti', 'Infiniti'),
        ('Isuzu', 'Isuzu'),
        ('Iveco', 'Iveco'),
        ('Jaguar', 'Jaguar'),
        ('Jeep', 'Jeep'),
        ('Kia', 'Kia'),
        ('Lada', 'Lada'),
        ('Lancia', 'Lancia'),
        ('Land Rover', 'Land Rover'),
        ('Lexus', 'Lexus'),
        ('Ligier', 'Ligier'),
        ('Lincoln', 'Lincoln'),
        ('Lotus', 'Lotus'),
        ('MAN', 'MAN'),
        ('Maserati', 'Maserati'),
        ('Maybach', 'Maybach'),
        ('Mazda', 'Mazda'),
        ('Mercedes', 'Mercedes'),
        ('Mercury', 'Mercury'),
        ('MG', 'MG'),
        ('Microcar', 'Microcar'),
        ('Mini', 'Mini'),
        ('Mitsubishi', 'Mitsubishi'),
        ('Morgan', 'Morgan'),
        ('Moskvich', 'Moskvich'),
        ('Nissan', 'Nissan'),
        ('Oldsmobile', 'Oldsmobile'),
        ('Opel', 'Opel'),
        ('Peugeot', 'Peugeot'),
        ('Piaggio', 'Piaggio'),
        ('Pontiac', 'Pontiac'),
        ('Porcshe', 'Porcshe'),
        ('Renault', 'Renault'),
        ('Rolls-Royce', 'Rolls-Royce'),
        ('Rover', 'Rover'),
        ('Saab', 'Saab'),
        ('Santana', 'Santana'),
        ('Scion', 'Scion'),
        ('Seat', 'Seat'),
        ('Skoda', 'Skoda'),
        ('Smart', 'Smart'),
        ('Subaru', 'Subaru'),
        ('Suzuki', 'Suzuki'),
        ('Tesla', 'Tesla'),
        ('Toyota', 'Toyota'),
        ('Triumph', 'Triumph'),
        ('UAZ', 'UAZ'),
        ('Vauxhall', 'Vauxhall'),
        ('Volkswagen', 'Vokswagen'),
        ('Volvo', 'Volvo')
    ]

    number = models.CharField(max_length=6, unique=True, validators=[validate_number])
    maker = models.CharField(max_length=32, choices=MANUFACTURERS)
    manufacturing_date = models.DateField(validators=[validate_manufacturing_date])
    series = models.CharField(max_length=3, auto_created=True)
    create_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('number',)

    def __str__(self):
        return self.number

    def save(self, *args, **kwargs):
        self.series = self.number[:3]
        super().save(*args, **kwargs)





