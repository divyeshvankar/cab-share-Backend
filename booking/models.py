from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

CAB_TYPE = (
    ('SUV', 'SUV'),
    ('Sedan', 'Sedan'),
    ('Innova', 'Innova'),
    ('Innova Crysta', 'Innova Crysta'),
    ('other', 'other'),
)

TRIP_TYPE = (
    ('Oneway', 'Oneway'),
    ('Round', 'Round'),
    ('Rental', 'Rental'),
    ('other', 'other'),
)

class Book(models.Model):
    name= models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    pickup = models.CharField(max_length=100)
    drop = models.CharField(max_length=100)
    cab_type = models.CharField(max_length=100,
                              choices=CAB_TYPE,
                              )
    trip_type = models.CharField(max_length=100,
                              choices=TRIP_TYPE,
                              )
    
    def __str__(self):
        return self.name