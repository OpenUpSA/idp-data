from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("idp_data", include("idp_data.idp_data.urls"),),
    path("admin/", admin.site.urls),
    path('api/v1/events', views.events, name="events"),
    path('api/v1/municipality', views.geography_detail, name="geo"),
    path('ckeditor', include('ckeditor_uploader.urls')),
]
