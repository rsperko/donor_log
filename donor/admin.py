from django.contrib import admin
from donor.models import Donor, Phone, Address, Donation, DonorContact

class PhoneInline(admin.StackedInline):
    model = Phone
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
    list_display = ('institution_name', 'last_name', 'first_name', 'type', 'email', 'added')
    fieldsets = [

    ]
    inlines = [
        PhoneInline,
        AddressInline,
        DonationInline,
        DonorContactInline,
    ]

# Register your models here.
admin.site.register(Donor, DonorAdmin)
