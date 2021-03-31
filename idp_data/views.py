from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from idp_data.idp_data.models import Event, Municipality, MunicipalityHostname, Category, EventSubmission
from idp_data.idp_data.serializers import EventSerializer, MunicipalitySerializer, CategorySerializer, EventSubmissionSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Case, CharField, Value, When
from rest_framework import status
from rest_framework.parsers import JSONParser

class Index(generic.TemplateView):
    template_name = "index.html"

@api_view(['GET'])
def events(request):
    host = request.GET.get('hostname', '')
    data = Event.objects.filter(muni__municipalityhostname__hostname=host)
    data = sorted(
        data,
        key=lambda event: event.start_date or event.end_date
    )
    serializer = EventSerializer(data, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def categories(_request):
    data = Category.objects
    serializer = CategorySerializer(data, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def geography_detail(request):
    host = request.GET.get('hostname', '')
    muni = get_object_or_404(Municipality, municipalityhostname__hostname=host)
    serializer = MunicipalitySerializer(muni, many=False)

    return Response(serializer.data)

@api_view(['GET', 'POST'])
def event_submissions(request):
    if request.POST:
        event_submission_data = request.data
        event_submission_serializer = EventSubmissionSerializer(data=event_submission_data)

        if event_submission_serializer.is_valid():
            event_submission_serializer.save()
            return Response(event_submission_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(event_submission_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.GET:
        data = EventSubmission.objects
        serializer = EventSubmissionSerializer(data, many=True)

        return Response(serializer.data)
    else:
        return Response("Unsupoorted method")

#TODO: Do not expose this in production
#@api_view(['GET'])
#def event_submissions_details():
