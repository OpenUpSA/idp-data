from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from idp_data.idp_data.models import Event, Municipality, MunicipalityHostname
from idp_data.idp_data.serializers import EventSerializer, MunicipalitySerializer
from django.shortcuts import get_object_or_404


class Index(generic.TemplateView):
    template_name = "index.html"


@api_view(['GET'])
def events(request):
    host = request.GET.get('hostname', '')
    data = Event.objects.filter(muni__municipalityhostname__hostname=host)
    serializer = EventSerializer(data, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def geography_detail(request):
    host = request.GET.get('hostname', '')
    muni = get_object_or_404(Municipality, municipalityhostname__hostname=host)
    serializer = MunicipalitySerializer(muni, many=False)

    return Response(serializer.data)
