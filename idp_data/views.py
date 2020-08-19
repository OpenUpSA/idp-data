from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from idp_data.idp_data.models import Event, Municipality, HostnameMunicipality
from idp_data.idp_data.serializers import EventSerializer, MunicipalitySerializer


class Index(generic.TemplateView):
    template_name = "index.html"


@api_view(['GET'])
def events(request, host):
    hostMuni = HostnameMunicipality.objects.filter(hostname=host)
    muni = hostMuni[0].muni
    data = Event.objects.filter(muni=muni.id)
    serializer = EventSerializer(data, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def geography_detail(request, host):
    # Events.objects.filter(muni__hostname=hostname)
    hostMuni = HostnameMunicipality.objects.filter(hostname=host)
    muni = hostMuni[0].muni
    serializer = MunicipalitySerializer(muni, many=False)

    return Response(serializer.data)