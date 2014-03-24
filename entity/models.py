from django.core import urlresolvers
from django.db import models
import datetime
from client.models import ClientInformation
from volunteer.models import VolunteerInformation

# Create your models here.


class Entity(models.Model):
    added = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=50,
                                  blank=True,
                                  null=True)
    last_name = models.CharField(max_length=50,
                                 blank=True,
                                 null=True)
    institution_name = models.CharField(max_length=100,
                                        blank=True,
                                        null=True)
    email = models.EmailField(blank=True,
                              null=True)
    notes = models.TextField(blank=True,
                             null=True)
    client_information = models.OneToOneField(ClientInformation,
                                              null=True,
                                              blank=True,
                                              related_name='client_information')
    volunteer_information = models.OneToOneField(VolunteerInformation,
                                              null=True,
                                              blank=True,
                                              related_name='volunteer_information')
    active = models.BooleanField(default=True)

    def name(self):
        if self.institution_name:
            return self.institution_name
        else:
            return self.last_name + ', ' + self.first_name

    def is_donor(self):
        return self.donor_information.count() > 0

    def is_client(self):
        return self.client_information is not None

    def donorinformation_link(self):
        if self.is_donor():
            changeform_url = urlresolvers.reverse('admin:donor_donorinformation_change', args=(self.donor_information.first().id,))
            return u'<a href="%s" target="_blank">Details</a>' % changeform_url
        return u''
    donorinformation_link.allow_tags = True
    donorinformation_link.short_description = 'Donor Information'



class Phone(models.Model):
    TYPE_HOME = 'H'
    TYPE_MOBILE = 'M'
    TYPE_WORK = 'W'
    TYPE_OTHER = 'O'
    TYPES = {
        TYPE_HOME: 'Home',
        TYPE_MOBILE: 'Mobile',
        TYPE_WORK: 'Work',
        TYPE_OTHER: 'Other',
    }
    entity = models.ForeignKey(Entity, related_name='phones')
    primary = models.BooleanField()
    number = models.CharField(max_length=12)
    type = models.CharField(max_length=1,
                            choices=tuple(sorted(TYPES.items())),
                            default=TYPE_MOBILE)

class Address(models.Model):
    entity = models.ForeignKey(Entity, related_name='addresses')
    primary = models.BooleanField()
    care_of = models.CharField(max_length=100,
                               blank=True,
                               null=True)
    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100,
                             blank=True,
                             null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    postalCode = models.CharField(max_length=10)


class Contact(models.Model):
    TYPE_PHONE = 'P'
    TYPE_EMAIL = 'E'
    TYPE_IN_PERSON = 'I'
    TYPE_OTHER = 'O'
    TYPES = {
        TYPE_EMAIL: 'E-mail',
        TYPE_IN_PERSON: 'In-Person',
        TYPE_PHONE: 'Phone',
        TYPE_OTHER: 'Other - see notes',
    }
    entity = models.ForeignKey(Entity)
    date_time = models.DateTimeField(default=datetime.datetime.now())
    type = models.CharField(max_length=1,
                            choices=tuple(sorted(TYPES.items())),
                            default=TYPE_PHONE)
    notes = models.TextField()


META_DATA = {
    'PHONE': {'TYPES': Phone.TYPES},
    'CONTACT': {'TYPES': Contact.TYPES},
}