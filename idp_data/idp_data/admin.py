import json
from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.functions import TruncDay
from django.db.models import Count

from .models import Event, Category, Municipality, EventAction, MunicipalityHostname, EventSubmission


class EventActionInline(admin.StackedInline):
    model = EventAction

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name', 'group')
    list_filter = ['group']

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

        filtered_chart_data = (queryset.annotate(date=TruncDay("submitted"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date"))
        
        all_chart_data = (EventSubmission.objects.annotate(date=TruncDay("submitted"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date"))

        filtered_chart_data_json = json.dumps(list(filtered_chart_data), cls=DjangoJSONEncoder)
        all_chart_data_json = json.dumps(list(all_chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": filtered_chart_data_json, "all_chart_data": all_chart_data_json}

        return super().changelist_view(request, extra_context=extra_context)

    def event_muni(self, obj):
        return obj.event.muni.name


admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(EventSubmission, EventSubmissionAdmin)
admin.site.register(Municipality, MunicipalityAdmin)
