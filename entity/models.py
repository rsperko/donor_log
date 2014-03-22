from django.db import models
import datetime
from donor.models import DonorInformation
from client.models import ClientInformation

# Create your models here.

class Entity(models.Model):
    added = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    institution_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    notes = models.TextField()
    donor_information = models.OneToOneField(DonorInformation, blank=True)
    client_information = models.OneToOneField(ClientInformation, blank=True)


class Phone(models.Model):
    TYPE_HOME = 'H'
    TYPE_MOBILE = 'M'
    TYPE_WORK = 'W'
    TYPE_OTHER = 'O'
    TYPES = (
        (TYPE_HOME, 'Home'),
        (TYPE_MOBILE, 'Mobile'),
        (TYPE_WORK, 'Work'),
        (TYPE_OTHER, 'Other')
    )
    entity = models.ForeignKey(Entity, related_name='phones')
    primary = models.BooleanField()
    number = models.CharField(max_length=12)
    type = models.CharField(max_length=1,
                            choices=TYPES,
                            default=TYPE_MOBILE)

class Address(models.Model):
    entity = models.ForeignKey(Entity, related_name='addresses')
    primary = models.BooleanField()
    care_of = models.CharField(max_length=100)
    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    postalCode = models.CharField(max_length=10)


class Contact(models.Model):
    TYPE_PHONE = 'P'
    TYPE_EMAIL = 'E'
    TYPE_IN_PERSON = 'I'
    TYPE_OTHER = 'O'
    TYPES = (
        (TYPE_EMAIL, 'E-mail'),
        (TYPE_IN_PERSON, 'In-Person'),
        (TYPE_PHONE, 'Phone'),
        (TYPE_OTHER, 'Other - see notes')
    )
    entity = models.ForeignKey(Entity)
    date_time = models.DateTimeField(default=datetime.datetime.now())
    type = models.CharField(max_length=1,
                            choices=TYPES,
                            default=TYPE_PHONE)
    notes = models.TextField()
