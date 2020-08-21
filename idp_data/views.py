from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from idp_data.idp_data.models import Event, Municipality, HostnameMunicipality
from idp_data.idp_data.serializers import EventSerializer, MunicipalitySerializer
from django.shortcuts import get_object_or_404


class Index(generic.TemplateView):
    template_name = "index.html"


@api_view(['GET'])
def events(request, host):
    hostMuni = get_object_or_404(HostnameMunicipality, hostname=host)
    muni = hostMuni.muni
    data = Event.objects.filter(muni=muni.id)
    serializer = EventSerializer(data, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def geography_detail(request, host):
    hostMuni = get_object_or_404(HostnameMunicipality, hostname=host)
    muni = hostMuni.muni
    serializer = MunicipalitySerializer(muni, many=False)

    return Response(serializer.data)
