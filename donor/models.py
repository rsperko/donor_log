from django.db import models
import datetime

# Create your models here.
class Donor(models.Model):
    DONOR = 'D'
    PARTNER = 'P'
    DONOR_TYPES = (
        (DONOR, 'Donor'),
        (PARTNER, 'Partner')
    )
    CATEGORY_INDIVIDUAL = 'I'
    CATEGORY_BUSINESS = 'B'
    CATEGORY_NON_PROFIT = 'N'
    CATEGORY_FOUNDATION = 'F'
    CATEGORIES = (
        (CATEGORY_BUSINESS, 'Business'),
        (CATEGORY_FOUNDATION, 'Foundation'),
        (CATEGORY_INDIVIDUAL, 'Individual'),
        (CATEGORY_NON_PROFIT, 'Non-Profit')
    )
    added = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    institution_name = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=1,
                            choices=DONOR_TYPES,
                            default=DONOR)
    # category = models.CharField(max_length=1,
    #                             choices=CATEGORIES,
    #                             default=CATEGORY_INDIVIDUAL)
    email = models.EmailField()
    notes = models.TextField()

class Phone(models.Model):
    HOME = 'H'
    MOBILE = 'M'
    WORK = 'W'
    OTHER = 'O'
    PHONE_TYPES = (
        (HOME, 'Home'),
        (MOBILE, 'Mobile'),
        (WORK, 'Work'),
        (OTHER, 'Other')
    )
    donor = models.ForeignKey(Donor)
    preferred = models.BooleanField()
    number = models.CharField(max_length=12)
    type = models.CharField(max_length=1,
                            choices=PHONE_TYPES,
                            default=MOBILE)

class Address(models.Model):
    donor = models.ForeignKey(Donor)
    preferred = models.BooleanField('preferred address')
    care_of = models.CharField(max_length=100)
    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    postalCode = models.CharField(max_length=10)

class Donation(models.Model):
    FURNITURE = 'F'
    CLOTHING = 'C'
    HOUSEHOLD_ITEM = 'H'
    FOOD = 'D'
    MONEY = 'M'
    OTHER = 'O'
    DONATION_TYPES = (
        (CLOTHING, 'Clothing'),
        (FOOD, 'Food'),
        (FURNITURE, 'Furniture'),
        (HOUSEHOLD_ITEM, 'Household Items'),
        (MONEY, 'Money'),
        (OTHER, 'Other')
    )
    donor = models.ForeignKey(Donor)
    date = models.DateField(default=datetime.date.today)
    monetary_amount = models.DecimalField(decimal_places=2, max_digits=8)
    in_kind = models.BooleanField()
    # type = models.CharField(max_length=1,
    #                         choices=DONATION_TYPES,
    #                         default=HOUSEHOLD_ITEM)
    notes = models.TextField()

class DonorContact(models.Model):
    PHONE = 'P'
    EMAIL = 'E'
    IN_PERSON = 'I'
    CONTACT_TYPES = (
        (EMAIL, 'E-mail'),
        (IN_PERSON, 'In-Person'),
        (PHONE, 'Phone')
    )
    donor = models.ForeignKey(Donor)
    date_time = models.DateTimeField(default=datetime.datetime.now())
    type = models.CharField(max_length=1,
                            choices=CONTACT_TYPES,
                            default=PHONE)
    notes = models.TextField()
