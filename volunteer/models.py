from django.db import models

import datetime

# Create your models here.


class AvailableHours(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()


class Availability(models.Model):
    sunday = models.OneToOneField(AvailableHours,
                                  null=True,
                                  related_name='sunday')
    monday = models.OneToOneField(AvailableHours,
                                  null=True,
                                  related_name='monday')
    tuesday = models.OneToOneField(AvailableHours,
                                   null=True,
                                   related_name='tuesday')
    wednesday = models.OneToOneField(AvailableHours,
                                     null=True,
                                     related_name='wednesday')
    thursday = models.OneToOneField(AvailableHours,
                                    null=True,
                                    related_name='thursday')
    friday = models.OneToOneField(AvailableHours,
                                  null=True,
                                  related_name='friday')
    saturday = models.OneToOneField(AvailableHours,
                                    null=True,
                                    related_name='saturday')


class VolunteerInformation(models.Model):
    active = models.BooleanField(default=True)
    availability = models.OneToOneField(Availability,
                                        null=True,
                                        blank=True,
                                        related_name='availability')


class Skill(models.Model):
    TYPE_DATA_ENTRY = 'D'
    TYPE_EVENTS = 'E'
    TYPE_SORTING = 'S'
    TYPE_WAREHOUSE = 'W'
    TYPE_OTHER = 'O'
    TYPES = {
        TYPE_DATA_ENTRY: 'Data Entry',
        TYPE_EVENTS: 'Events',
        TYPE_SORTING: 'Sorting',
        TYPE_WAREHOUSE: 'Warehouse',
        TYPE_OTHER: 'Other - see notes',
        }
    volunteer = models.ForeignKey(VolunteerInformation, related_name='skills')
    type = models.CharField(max_length=1,
                            choices=tuple(TYPES.items()),
                            default=TYPE_SORTING)
    notes = models.TextField(blank=True)


META_DATA = {
    'SKILLS': {'TYPES': Skill.TYPES},
}