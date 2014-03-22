from django.db import models

import datetime

# Create your models here.

# Create your models here.


class ClientInformation(models.Model):
    TYPE_INDIVIDUAL = 'I'
    TYPE_FAMILY = 'F'
    TYPES = (
        (TYPE_INDIVIDUAL, 'Individual'),
        (TYPE_FAMILY, 'Family'),
    )
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
    notes = models.TextField(blank=True)


class FamilyMember(models.Model):
    TYPE_CHILD = 'C'
    TYPE_SPOUSE = 'S'
    TYPE_PARENT = 'P'
    TYPE_SIBLING = 'I'
    TYPES = (
        (TYPE_CHILD, 'Child'),
        (TYPE_SPOUSE, 'Spouse'),
        (TYPE_PARENT, 'Parent'),
        (TYPE_SIBLING, 'Sibling'),
    )
    SEX_MALE = 'M'
    SEX_FEMALE = 'F'
    SEXES = (
        (SEX_FEMALE, 'Female'),
        (SEX_MALE, 'Male')
    )
    client = models.ForeignKey(ClientInformation, related_name='family_members')
    type = models.CharField(max_length=1,
                            choices=TYPES,
                            default=TYPE_CHILD)
    name = models.CharField(max_length=100,
                            blank=True,
                            null=True)
    birth_date = models.DateField(null=True,
                            blank=True)
    sex = models.CharField(max_length=1,
                           choices=SEXES,
                           default=SEX_FEMALE)



META_DATA = (
    'CLIENT_INFORMATION', ('TYPES', ClientInformation.TYPES),
    'SERVICE', ('TYPES', Service.TYPES),
    'FAMILY_MEMBER', ('TYPES', FamilyMember.TYPES),
)