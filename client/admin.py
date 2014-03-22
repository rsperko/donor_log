from django.contrib import admin
from client.models import *
# Register your models here.


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 0


class ClientInformationAdmin(admin.ModelAdmin):
    list_display = ('type',)
    fieldsets = []
    inlines = [
        ServiceInline,
    ]


# Register your models here.
admin.site.register(ClientInformation, ClientInformationAdmin)