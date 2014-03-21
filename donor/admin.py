from django.contrib import admin
from donor.models import Donor, Phone, Address, Donation, DonorContact

class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 0

class AddressInline(admin.TabularInline):
    model = Address
    extra = 0

class DonationInline(admin.TabularInline):
    model = Donation
    extra = 0

class DonorContactInline(admin.TabularInline):
    model = DonorContact
    extra = 0

class DonorAdmin(admin.ModelAdmin):
    list_display = ('type', 'institution_name', 'last_name', 'first_name', 'email', 'added')
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
