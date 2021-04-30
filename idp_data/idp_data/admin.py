import json
from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.functions import TruncDay
from django.db.models import Count

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
    list_filter = ('submitter_town', 'submission_issue', 'event')

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context)
        queryset = response.context_data["cl"].queryset
        chart_data = (queryset.annotate(date=TruncDay("submitted"))
                      .values("date")
                      .annotate(y=Count("id"))
                      .order_by("-date"))
        
        all_chart_data = (EventSubmission.objects.annotate(date=TruncDay("submitted"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date"))

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        all_as_json = json.dumps(list(all_chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json, "all_chart_data": all_as_json}

        #as_json[0] = {"date": "2021-03-1T00:00:00Z", "y": 0}
        print(as_json)

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)

    def event_muni(self, obj):
        return obj.event.muni.name


admin.site.register(Event, EventAdmin)
admin.site.register(Category)
admin.site.register(EventSubmission, EventSubmissionAdmin)
admin.site.register(Municipality, MunicipalityAdmin)
