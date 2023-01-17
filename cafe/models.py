from django.db import models
from django.db.models import Model, CharField, URLField, IntegerField, BooleanField
from multiselectfield import MultiSelectField

# Create your models here.

class CafeModel(Model):
    name = CharField(max_length=100, null=False, unique=True)
    ratings_choices = (
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    ratings = CharField(max_length=100, choices=ratings_choices)
    timing = CharField(max_length=100, null=False)
    address = CharField(max_length=150, null=False, unique=True)
    url = URLField()
    services_choices = (
        ("Coffee", "Coffee"),
        ("Food", "Food"),
        ("Veggies", "Veggies"),
        ("Alcohol", "Alcohol"),
        ("Cards", "Cards"),
    )
    services = MultiSelectField(max_length=150, choices=services_choices)
    tables = IntegerField()
    wifi = BooleanField()
    sockets = IntegerField()
    long_stays = BooleanField()
    quiet = BooleanField()
    calls = BooleanField()

    def __str__(self) :
        return self.name