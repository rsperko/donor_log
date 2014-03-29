from django.contrib import admin

from .models import Phone, Address, Communication, Entity, \
    ClientInformation, Service, FamilyMember, \
    DonorInformation, Donation, \
    VolunteerInformation, Skill


# Register your models here.
class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 0


class AddressInline(admin.TabularInline):
    model = Address
    extra = 0


class CommunicationInline(admin.TabularInline):
    model = Communication
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
        CommunicationInline,
    ]


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 0


class FamilyMemberInline(admin.TabularInline):
    model = FamilyMember
    extra = 0


class ClientInformationAdmin(admin.ModelAdmin):
    list_display = ('type',)
    fieldsets = []
    inlines = [
        FamilyMemberInline,
        ServiceInline,
    ]


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


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0


class VolunteerInformationAdmin(admin.ModelAdmin):
    list_display = ('active',)
    fieldsets = []
    inlines = [
        SkillInline,
    ]


# Register your models here.
admin.site.register(Entity, EntityAdmin)
admin.site.register(DonorInformation, DonorInformationAdmin)
admin.site.register(ClientInformation, ClientInformationAdmin)
admin.site.register(VolunteerInformation, VolunteerInformationAdmin)