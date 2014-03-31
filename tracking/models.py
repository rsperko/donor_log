from django.core import urlresolvers
from django.db import models
import datetime

# Create your models here.


class Entity(models.Model):
    added = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=50,
                                  blank=True)
    last_name = models.CharField(max_length=50,
                                 blank=True)
    institution_name = models.CharField(max_length=100,
                                        blank=True)
    email = models.EmailField(blank=True)
    notes = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def name(self):
        if self.institution_name:
            return self.institution_name
        else:
            return self.last_name + ', ' + self.first_name

    def is_donor(self):
        return self.donor_information.count() > 0

    def is_client(self):
        return self.client_information.count() > 0

    def is_volunteer(self):
        return self.volunteer_information.count() > 0

    def donorinformation_link(self):
        if self.is_donor():
            changeform_url = urlresolvers.reverse('admin:donor_donorinformation_change', args=(self.donor_information.first().id,))
            return u'<a href="%s" target="_blank">Details</a>' % changeform_url
        return u''
    donorinformation_link.allow_tags = True
    donorinformation_link.short_description = 'Donor Information'

    def clientinformation_link(self):
        if self.is_client():
            changeform_url = urlresolvers.reverse('admin:client_clientinformation_change', args=(self.client_information.first().id,))
            return u'<a href="%s" target="_blank">Details</a>' % changeform_url
        return u''
    clientinformation_link.allow_tags = True
    clientinformation_link.short_description = 'Client Information'

    def volunteerinformation_link(self):
        if self.is_volunteer():
            changeform_url = urlresolvers.reverse('admin:volunteer_volunteerinformation_change', args=(self.volunteer_information.first().id,))
            return u'<a href="%s" target="_blank">Details</a>' % changeform_url
        return u''
    volunteerinformation_link.allow_tags = True
    volunteerinformation_link.short_description = 'Volunteer Information'



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
                               blank=True)
    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100,
                             blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    postalCode = models.CharField(max_length=10)


class Communication(models.Model):
    TYPE_PHONE = 'P'
    TYPE_EMAIL = 'E'
    TYPE_IN_PERSON = 'I'
    TYPE_OTHER = 'O'
    TYPES = {
        TYPE_EMAIL: 'E-mail',
        TYPE_IN_PERSON: 'In-Person',
        TYPE_PHONE: 'Phone',
        TYPE_OTHER: 'Other',
    }
    entity = models.ForeignKey(Entity, related_name='communications')
    date = models.DateField(default=datetime.date.today)
    type = models.CharField(max_length=1,
                            choices=tuple(sorted(TYPES.items())),
                            default=TYPE_PHONE)
    notes = models.TextField()
    connected = models.BooleanField()


class ClientInformation(models.Model):
    TYPE_INDIVIDUAL = 'I'
    TYPE_FAMILY = 'F'
    TYPE_UNSET = 'U'
    TYPES = {
        TYPE_INDIVIDUAL: 'Individual',
        TYPE_FAMILY: 'Family',
        TYPE_UNSET: 'Unset'
    }
    entity = models.ForeignKey(Entity,
                               related_name='client_information')
    type = models.CharField(max_length=1,
                            choices=tuple(sorted(TYPES.items())),
                            default=TYPE_UNSET)

    def __str__(self):
        return self.TYPES[self.type]


class Service(models.Model):
    TYPE_FURNITURE = 'F'
    TYPE_CLOTHING = 'C'
    TYPE_HOUSEHOLD_ITEM = 'H'
    TYPE_FOOD = 'D'
    TYPE_OTHER = 'O'
    TYPES = {
        TYPE_CLOTHING: 'Clothing',
        TYPE_FOOD: 'Food',
        TYPE_FURNITURE: 'Furniture',
        TYPE_HOUSEHOLD_ITEM: 'Household Items',
        TYPE_OTHER: 'Other'
    }
    client = models.ForeignKey(ClientInformation, related_name='services')
    date = models.DateField(default=datetime.date.today)
    type = models.CharField(max_length=1,
                            choices=tuple(sorted(TYPES.items())),
                            default=TYPE_HOUSEHOLD_ITEM)
    notes = models.TextField(blank=True)


class FamilyMember(models.Model):
    TYPE_CHILD = 'C'
    TYPE_SPOUSE = 'S'
    TYPE_PARENT = 'P'
    TYPE_SIBLING = 'I'
    TYPES = {
        TYPE_CHILD: 'Child',
        TYPE_SPOUSE: 'Spouse',
        TYPE_PARENT: 'Parent',
        TYPE_SIBLING: 'Sibling',
    }
    SEX_MALE = 'M'
    SEX_FEMALE = 'F'
    SEXES = {
        SEX_FEMALE: 'Female',
        SEX_MALE: 'Male',
    }
    client = models.ForeignKey(ClientInformation, related_name='family_members')
    type = models.CharField(max_length=1,
                            choices=tuple(sorted(TYPES.items())),
                            default=TYPE_CHILD)
    name = models.CharField(max_length=100,
                            blank=True)
    birth_date = models.DateField(null=True,
                                  blank=True)
    sex = models.CharField(max_length=1,
                           choices=tuple(sorted(SEXES.items())),
                           default=SEX_FEMALE)


class DonorInformation(models.Model):
    TYPE_DONOR = 'D'
    TYPE_PARTNER = 'P'
    TYPES = {
        TYPE_DONOR: 'Donor',
        TYPE_PARTNER: 'Partner',
    }
    CATEGORY_INDIVIDUAL = 'I'
    CATEGORY_BUSINESS = 'B'
    CATEGORY_NON_PROFIT = 'N'
    CATEGORY_FOUNDATION = 'F'
    CATEGORY_OTHER = 'O'
    CATEGORY_UNSET = 'U'
    CATEGORIES = {
        CATEGORY_BUSINESS: 'Business',
        CATEGORY_FOUNDATION: 'Foundation',
        CATEGORY_INDIVIDUAL: 'Individual',
        CATEGORY_NON_PROFIT: 'Non-Profit',
        CATEGORY_OTHER: 'Other',
        CATEGORY_UNSET: 'Unset',
    }
    entity = models.ForeignKey(Entity,
                               related_name='donor_information')
    category = models.CharField(max_length=1,
                                choices=tuple(sorted(CATEGORIES.items())),
                                default=CATEGORY_UNSET)
    type = models.CharField(max_length=1,
                            choices=tuple(sorted(TYPES.items())),
                            default=TYPE_DONOR)


class Donation(models.Model):
    TYPE_FURNITURE = 'F'
    TYPE_CLOTHING = 'C'
    TYPE_HOUSEHOLD_ITEM = 'H'
    TYPE_FOOD = 'D'
    TYPE_MONEY = 'M'
    TYPE_OTHER = 'O'
    TYPE_IN_KIND = 'I'
    TYPES = {
        TYPE_CLOTHING: 'Clothing',
        TYPE_FOOD: 'Food',
        TYPE_FURNITURE: 'Furniture',
        TYPE_HOUSEHOLD_ITEM: 'Household Items',
        TYPE_MONEY: 'Money',
        TYPE_IN_KIND: 'In-Kind',
        TYPE_OTHER: 'Other',
    }
    donor = models.ForeignKey(DonorInformation, related_name='donations')
    date = models.DateField(default=datetime.date.today)
    monetary_amount = models.DecimalField(decimal_places=2,
                                          max_digits=8,
                                          blank=True)
    type = models.CharField(max_length=1,
                            choices=tuple(sorted(TYPES.items())),
                            default=TYPE_HOUSEHOLD_ITEM)
    notes = models.TextField(blank=True)


class VolunteerInformation(models.Model):
    entity = models.ForeignKey(Entity,
                               related_name='volunteer_information')
    active = models.BooleanField(default=True)
    emergency_contact_name = models.CharField(max_length=50,
                                              blank=True)
    emergency_contact_number = models.CharField(max_length=12,
                                                blank=True)

    def __str__(self):
        return "active: " + str(self.active)


class Skill(models.Model):
    TYPE_DATA_ENTRY = 'D'
    TYPE_EVENTS = 'E'
    TYPE_SORTING = 'S'
    TYPE_WAREHOUSE = 'W'
    TYPE_SPEAKING = 'P'
    TYPE_OTHER = 'O'
    TYPES = {
        TYPE_DATA_ENTRY: 'Data Entry',
        TYPE_EVENTS: 'Events',
        TYPE_SORTING: 'Sorting',
        TYPE_WAREHOUSE: 'Warehouse',
        TYPE_OTHER: 'Other',
        TYPE_SPEAKING: 'Public Speaking',
    }
    volunteer = models.ForeignKey(VolunteerInformation, related_name='skills')
    type = models.CharField(max_length=1,
                            choices=tuple(sorted(TYPES.items())),
                            default=TYPE_SORTING)

COMMON_META_DATA = {

}


VOLUNTEER_META_DATA = {
    'skill': {'types': Skill.TYPES},
}


DONOR_META_DATA = {
    'donor_information': {
        'categories': DonorInformation.CATEGORIES,
        'types': DonorInformation.TYPES,
    },
    'donation': {'types': Donation.TYPES},
}


CLIENT_META_DATA = {
    'client_information': {'types': ClientInformation.TYPES},
    'service': {'types': Service.TYPES},
    'family_member': {'types': FamilyMember.TYPES, 'sexes': FamilyMember.SEXES},
}

ENTITY_META_DATA = {
    'phone': {'types': Phone.TYPES},
    'communication': {'types': Communication.TYPES},
    'address' : {
        'states': {
            'AL': 'Alabama',
            'AK': 'Alaska',
            'AS': 'American Samoa',
            'AZ': 'Arizona',
            'AR': 'Arkansas',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DE': 'Delaware',
            'DC': 'Dist. of Columbia',
            'FL': 'Florida',
            'GA': 'Georgia',
            'GU': 'Guam',
            'HI': 'Hawaii',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'IA': 'Iowa',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'ME': 'Maine',
            'MD': 'Maryland',
            'MH': 'Marshall Islands',
            'MA': 'Massachusetts',
            'MI': 'Michigan',
            'FM': 'Micronesia',
            'MN': 'Minnesota',
            'MS': 'Mississippi',
            'MO': 'Missouri',
            'MT': 'Montana',
            'NE': 'Nebraska',
            'NV': 'Nevada',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NY': 'New York',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'MP': 'Northern Marianas',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PW': 'Palau',
            'PA': 'Pennsylvania',
            'PR': 'Puerto Rico',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VT': 'Vermont',
            'VA': 'Virginia',
            'VI': 'Virgin Islands',
            'WA': 'Washington',
            'WV': 'West Virginia',
            'WI': 'Wisconsin',
            'WY': 'Wyoming',
        }
    }
}