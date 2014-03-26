from django.contrib import admin
from volunteer.models import *
# Register your models here.


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0


class AvailableHoursAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time',)


class AvailableHoursInline(admin.TabularInline):
    model = AvailableHours


class AvailabilityInline(admin.TabularInline):
    model = Availability


class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ()
    fieldsets = []
    inlines = [
        AvailableHoursInline,
    ]


class VolunteerInformationAdmin(admin.ModelAdmin):
    list_display = ('active',)
    fieldsets = []
    inlines = [
        AvailabilityInline,
        SkillInline,
        ]


# Register your models here.
admin.site.register(VolunteerInformation, VolunteerInformationAdmin)
admin.site.register(Availability, AvailabilityAdmin)
admin.site.register(AvailableHours, AvailableHoursAdmin)
