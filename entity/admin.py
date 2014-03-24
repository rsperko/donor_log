from django.contrib import admin

from entity.models import *

from donor.models import DonorInformation
from client.models import ClientInformation
from volunteer.models import VolunteerInformation

# Register your models here.


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 0


class AddressInline(admin.TabularInline):
    model = Address
    extra = 0


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 0


class DonorInformationInline(admin.StackedInline):
    model = DonorInformation
    extra = 0


class ClientInformationInline(admin.StackedInline):
    model = ClientInformation
    extra = 0


class VolunteerInformationInline(admin.StackedInline):
    model = VolunteerInformation
    extra = 0


class EntityAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'email',
                    'is_donor',
                    'is_client',
                    'is_volunteer',
                    'added',)
    fields = (
        'first_name',
        'last_name',
        'institution_name',
        'email',
        'notes',
        'active',
        'donorinformation_link',
        'clientinformation_link',
        'volunteerinformation_link',
    )
    readonly_fields = (
        'donorinformation_link',
        'clientinformation_link',
        'volunteerinformation_link',
    )
    fieldsets = []
    inlines = [
        DonorInformationInline,
        ClientInformationInline,
        VolunteerInformationInline,
        PhoneInline,
        AddressInline,
        ContactInline,
    ]

# Register your models here.
admin.site.register(Entity, EntityAdmin)
