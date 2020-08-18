from django.contrib import admin
from .models import Event, Category, Municipality, EventAction


admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Municipality)
admin.site.register(EventAction)