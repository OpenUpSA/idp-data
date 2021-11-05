from django.db import models
from datetime import date
from ckeditor.fields import RichTextField
from django.contrib.postgres.fields import JSONField



class Category(models.Model):
    name = models.CharField(max_length=500)
    icon = models.CharField(max_length=50, default='')
    description = RichTextField(max_length=1000, default='',help_text="This is shown to users.")
    group = models.CharField(max_length=255,default='',null=True,help_text='The heading this info will be grouped under')

    def __str__(self):
        return self.name


class Municipality(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    homepage_url = models.CharField(max_length=500,verbose_name="Homepage URL")
    by_laws_url = models.CharField(max_length=500,verbose_name="By Laws URL")
    financial_performance_url = models.CharField(max_length=500,verbose_name="Financial Performance URL",default="")
    ward_councillor_url = models.CharField(max_length=500,verbose_name="Find Your Ward Councillor URL")
    page_title = models.CharField(max_length=200,verbose_name="Page Title",default="Public Participation Guide")
    colour_primary_fill = models.CharField(max_length=6,verbose_name="Custom primary fill colour",help_text="CSS hex colour code e.g. ff8c00",default='ff8c00')
    colour_primary_text = models.CharField(max_length=6,verbose_name="Custom primary text colour",help_text="CSS hex colour code e.g. ff8c00",default='ff8c00')
    towns = JSONField(default=dict)
    event_submission_email_address = models.EmailField(max_length=254, null=True, blank=True, help_text="The email address any event submissions (comments) should be sent to.")
    enquiry_email_address = models.EmailField(max_length=254, null=True, blank=True, help_text="The email address shown after event submissions.")
    event_submission_form_enabled = models.BooleanField(default=False,help_text='Whether this municipality will show the comment form for active engagements.')
    post_submission_message = RichTextField(blank=True, null=True, help_text="Shown after an even submission has been made.")

    def __str__(self):
        return self.code


class MunicipalityHostname(models.Model):
    muni = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    hostname = models.CharField(max_length=200)

    def __str__(self):
        return self.hostname


class Event(models.Model):
    archived = models.BooleanField(default=False)
    muni = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    short_desc = models.TextField(max_length=500,help_text="Max. 500 characters")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=False)
    comment_open_date = models.DateField(blank=True, null=True)
    comment_close_date = models.DateField(blank=True, null=True)
    modal_information = RichTextField(blank=True, null=True, help_text="Shown in modal but not on card.")

    def __str__(self):
        return self.title

class EventAction(models.Model):
    event = models.ForeignKey(Event, models.DO_NOTHING, related_name='actions')
    internal_label = models.CharField(max_length=500)
    icon = models.CharField(max_length=50, default='')
    confirmed_date = models.CharField(max_length=500)
    description_html = RichTextField(verbose_name="Description")
    extra = models.BooleanField(default=False,help_text='Extra actions are only shown in the modal')

    def __str__(self):
        return self.internal_label

class EventSubmission(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    submission = models.TextField(max_length=5000)
    #TODO: Better defaults
    submission_issue = models.CharField(max_length=500,default="Municipal")
    submitter_town = models.CharField(max_length=500,default="Bitterfontein")
    submitter_name = models.CharField(max_length=255)
    submitter_contact = models.CharField(max_length=255)
    submitted = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    recaptcha_score = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'#{self.id} - {self.event} - {self.submitter_name} - {self.submitted}'
