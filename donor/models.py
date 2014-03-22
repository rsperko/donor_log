from django.db import models
import datetime

# Create your models here.
class DonorInformation(models.Model):
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
    entity = models.OneToOneField(Entity)
    category = models.CharField(max_length=1,
                                choices=CATEGORIES,
                                default=CATEGORY_INDIVIDUAL)
    type = models.CharField(max_length=1,
                            choices=TYPES,
                            default=TYPE_DONOR)

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
    donor = models.ForeignKey(DonorInformation, related_name='donations')
    date = models.DateField(default=datetime.date.today)
    monetary_amount = models.DecimalField(decimal_places=2,
                                          max_digits=8)
    in_kind = models.BooleanField()
    type = models.CharField(max_length=1,
                            choices=TYPES,
                            default=TYPE_HOUSEHOLD_ITEM)
    notes = models.TextField()
