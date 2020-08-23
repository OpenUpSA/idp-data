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


class MunicipalityHostname(models.Model):
    muni = models.ForeignKey(Municipality, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)
    hostname = models.CharField(max_length=200)

    def __str__(self):
        return self.hostname


class Event(models.Model):
    muni = models.ForeignKey(Municipality, on_delete=models.CASCADE, default=None, blank=False, null=False)
    title = models.CharField(max_length=500)
    short_desc = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=False)

    def __str__(self):
        return self.title

class EventAction(models.Model):
    event = models.ForeignKey(Event, models.DO_NOTHING, related_name='actions')
    internal_label = models.CharField(max_length=500)
    icon = models.CharField(max_length=50, default='')
    confirmed_date = models.CharField(max_length=500)
    description_html = RichTextField(verbose_name="Description")

    def __str__(self):
        return self.internal_label