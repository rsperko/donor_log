from django.contrib import admin

from entity.models import *

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


class EntityAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'email',
                    'is_donor',
                    'is_client',
                    'added')
    fieldsets = [

    ]
    inlines = [
        PhoneInline,
        AddressInline,
        ContactInline,
    ]

# Register your models here.
admin.site.register(Entity, EntityAdmin)
