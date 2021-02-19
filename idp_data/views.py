from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from idp_data.idp_data.models import Event, Municipality, MunicipalityHostname, Category
from idp_data.idp_data.serializers import EventSerializer, MunicipalitySerializer, CategorySerializer
from django.shortcuts import get_object_or_404
from django.db.models import Case, CharField, Value, When


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
