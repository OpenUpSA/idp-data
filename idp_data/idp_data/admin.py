from django.contrib import admin
from .models import Event, Category, Municipality, EventAction, HostnameMunicipality

class EventActionInline(admin.StackedInline):
    model = EventAction

class EventAdmin(admin.ModelAdmin):
    inlines = [EventActionInline]

class HostnameMunicipalityInline(admin.StackedInline):
    model = HostnameMunicipality

class MunicipalityAdmin(admin.ModelAdmin):
    inlines = [HostnameMunicipalityInline]


admin.site.register(Event, EventAdmin)
admin.site.register(Category)
admin.site.register(Municipality, MunicipalityAdmin)