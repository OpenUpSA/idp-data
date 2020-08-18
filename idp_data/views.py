from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from idp_data.idp_data.models import Event, Municipality
from idp_data.idp_data.serializers import EventSerializer


class Index(generic.TemplateView):
    template_name = "index.html"


@api_view(['GET'])
def events(request, geo):
    muni = Municipality.objects.filter(code=geo)
    data = Event.objects.filter(muni=muni[0].id)
    serializer = EventSerializer(data, many=True)

    return Response(serializer.data)