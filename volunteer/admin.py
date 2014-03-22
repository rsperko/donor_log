from django.contrib import admin
from volunteer.models import *
# Register your models here.


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0


class AvailableHoursAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time',)


class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ()
    fieldsets = []
    inlines = []


class VolunteerInformationAdmin(admin.ModelAdmin):
    list_display = ('active',)
    fieldsets = []
    inlines = [
        SkillInline,
        ]


# Register your models here.
admin.site.register(VolunteerInformation, VolunteerInformationAdmin)
admin.site.register(Availability, AvailabilityAdmin)
admin.site.register(AvailableHours, AvailableHoursAdmin)
