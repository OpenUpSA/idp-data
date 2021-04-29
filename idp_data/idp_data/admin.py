from django.contrib import admin
from .models import Event, Category, Municipality, EventAction, MunicipalityHostname, EventSubmission


class EventActionInline(admin.StackedInline):
    model = EventAction


class EventAdmin(admin.ModelAdmin):
    inlines = [EventActionInline]


class MunicipalityHostnameInline(admin.StackedInline):
    model = MunicipalityHostname


class MunicipalityAdmin(admin.ModelAdmin):
    inlines = [MunicipalityHostnameInline]


class EventSubmissionAdmin(admin.ModelAdmin):
    model = EventSubmission
    date_hierarchy = 'submitted'
    list_display = ('submitted',
                    'event',
                    'submission_issue',
                    'submitter_town',
                    'submitter_name',
                    'submitter_contact',
                    'event_muni')

    def event_muni(self, obj):
        return obj.event.muni.name


admin.site.register(Event, EventAdmin)
admin.site.register(Category)
admin.site.register(EventSubmission, EventSubmissionAdmin)
admin.site.register(Municipality, MunicipalityAdmin)
