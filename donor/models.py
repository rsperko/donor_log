from django.db import models
import datetime

# Create your models here.
class Donor(models.Model):
    TYPE_DONOR = 'D'
    TYPE_PARTNER = 'P'
    TYPES = (
        (TYPE_DONOR, 'Donor'),
        (TYPE_PARTNER, 'Partner')
    )
    CATEGORY_INDIVIDUAL = 'I'
    CATEGORY_BUSINESS = 'B'
    CATEGORY_NON_PROFIT = 'N'
    CATEGORY_FOUNDATION = 'F'
    CATEGORY_OTHER = 'O'
    CATEGORIES = (
        (CATEGORY_BUSINESS, 'Business'),
        (CATEGORY_FOUNDATION, 'Foundation'),
        (CATEGORY_INDIVIDUAL, 'Individual'),
        (CATEGORY_NON_PROFIT, 'Non-Profit'),
        (CATEGORY_OTHER, 'Other - see notes')
    )
    added = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    institution_name = models.CharField(max_length=100, blank=True)
    # category = models.CharField(max_length=1,
    #                             choices=CATEGORIES,
    #                             default=CATEGORY_INDIVIDUAL)
    email = models.EmailField()
    notes = models.TextField()
    type = models.CharField(max_length=1,
                            choices=TYPES,
                            default=TYPE_DONOR)

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
    donor = models.ForeignKey(Donor)
    preferred = models.BooleanField()
    number = models.CharField(max_length=12)
    type = models.CharField(max_length=1,
                            choices=TYPES,
                            default=TYPE_MOBILE)

class Address(models.Model):
    donor = models.ForeignKey(Donor)
    preferred = models.BooleanField()
    care_of = models.CharField(max_length=100)
    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    postalCode = models.CharField(max_length=10)

class Donation(models.Model):
    TYPE_FURNITURE = 'F'
    TYPE_CLOTHING = 'C'
    TYPE_HOUSEHOLD_ITEM = 'H'
    TYPE_FOOD = 'D'
    TYPE_MONEY = 'M'
    TYPE_OTHER = 'O'
    TYPES = (
        (TYPE_CLOTHING, 'Clothing'),
        (TYPE_FOOD, 'Food'),
        (TYPE_FURNITURE, 'Furniture'),
        (TYPE_HOUSEHOLD_ITEM, 'Household Items'),
        (TYPE_MONEY, 'Money'),
        (TYPE_OTHER, 'Other - see notes')
    )
    donor = models.ForeignKey(Donor)
    date = models.DateField(default=datetime.date.today)
    monetary_amount = models.DecimalField(decimal_places=2,
                                          max_digits=8)
    in_kind = models.BooleanField()
    # type = models.CharField(max_length=1,
    #                         choices=DONATION_TYPES,
    #                         default=HOUSEHOLD_ITEM)
    notes = models.TextField()

class DonorContact(models.Model):
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
    donor = models.ForeignKey(Donor)
    date_time = models.DateTimeField(default=datetime.datetime.now())
    type = models.CharField(max_length=1,
                            choices=TYPES,
                            default=TYPE_PHONE)
    notes = models.TextField()
