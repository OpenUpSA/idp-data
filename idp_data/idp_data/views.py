from django.views import generic


class Index(generic.TemplateView):
    template_name = "idp_data/index.html"