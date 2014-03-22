from django.contrib import admin
from donor.models import *


class DonationInline(admin.TabularInline):
    model = Donation
    extra = 0


class DonorInformationAdmin(admin.ModelAdmin):
    list_display = ('type',
                    'category',
    )
    fieldsets = [
    ]
    inlines = [
        DonationInline,
    ]


# Register your models here.
admin.site.register(DonorInformation, DonorInformationAdmin)
