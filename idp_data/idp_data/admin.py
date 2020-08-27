from django.contrib import admin
from .models import Event, Category, Municipality, EventAction, MunicipalityHostname

class EventActionInline(admin.StackedInline):
    model = EventAction

class EventAdmin(admin.ModelAdmin):
    inlines = [EventActionInline]

class MunicipalityHostnameInline(admin.StackedInline):
    model = MunicipalityHostname

class MunicipalityAdmin(admin.ModelAdmin):
    inlines = [MunicipalityHostnameInline]


admin.site.register(Event, EventAdmin)
admin.site.register(Category)
admin.site.register(Municipality, MunicipalityAdmin)