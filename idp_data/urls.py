from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("idp_data", include("idp_data.idp_data.urls"),),
    path("admin/", admin.site.urls),
    path('api/v1/events', views.events, name="events"),
    path('api/v1/municipality', views.geography_detail, name="geo"),
    path('api/v1/categories', views.categories, name="category"),
    path('api/v1/event-submissions', views.event_submissions, name="event_submissions"),
    path('ckeditor', include('ckeditor_uploader.urls')),
]
