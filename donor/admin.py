from django.contrib import admin
from donor.models import Donor, Email, Address, Donation, DonorContact

class EmailInline(admin.StackedInline):
    model = Email
    extra = 0

class AddressInline(admin.StackedInline):
    model = Address
    extra = 0

class DonationInline(admin.StackedInline):
    model = Donation
    extra = 0

class DonorContactInline(admin.StackedInline):
    model = DonorContact
    extra = 0

class DonorAdmin(admin.ModelAdmin):
    fieldsets = [

    ]
    inlines = [
        EmailInline,
        AddressInline,
        DonationInline,
        DonorContactInline,
    ]

# Register your models here.
admin.site.register(Donor, DonorAdmin)
