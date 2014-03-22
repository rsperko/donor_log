from django.db import models

import datetime

from entity.models import Entity

# Create your models here.

# Create your models here.
class ClientInformation(models.Model):
    TYPE_INDIVIDUAL = 'I'
    TYPE_FAMILY = 'F'
    TYPES = (
        (TYPE_INDIVIDUAL, 'Individual'),
        (TYPE_FAMILY, 'Family'),
    )
    entity = models.OneToOneField(Entity)
    type = models.CharField(max_length=1,
                            choices=TYPES,
                            default=TYPE_INDIVIDUAL)

class Service(models.Model):
    TYPE_FURNITURE = 'F'
    TYPE_CLOTHING = 'C'
    TYPE_HOUSEHOLD_ITEM = 'H'
    TYPE_FOOD = 'D'
    TYPE_OTHER = 'O'
    TYPES = (
        (TYPE_CLOTHING, 'Clothing'),
        (TYPE_FOOD, 'Food'),
        (TYPE_FURNITURE, 'Furniture'),
        (TYPE_HOUSEHOLD_ITEM, 'Household Items'),
        (TYPE_OTHER, 'Other - see notes')
    )
    client = models.ForeignKey(ClientInformation, related_name='services')
    date = models.DateField(default=datetime.date.today)
    type = models.CharField(max_length=1,
                            choices=TYPES,
                            default=TYPE_HOUSEHOLD_ITEM)
    notes = models.TextField()
