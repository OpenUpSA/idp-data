from django.db import models
from datetime import date
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=500)
    icon = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name


class Municipality(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.code


class HostnameMunicipality(models.Model):
    muni = models.ForeignKey(Municipality, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)
    hostname = models.CharField(max_length=200)

    def __str__(self):
        return self.hostname


class Event(models.Model):
    muni = models.ForeignKey(Municipality, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)
    title = models.CharField(max_length=500)
    short_desc = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    confirmed_date = models.DateField("date added", default=date.today)

    def __str__(self):
        return self.title

class EventAction(models.Model):
    event = models.ForeignKey(Event, models.DO_NOTHING, related_name='actions')
    title = models.CharField(max_length=500)
    icon = models.CharField(max_length=50, default='')
    raw_html = RichTextField()  #models.CharField(max_length=500)

    def __str__(self):
        return self.title