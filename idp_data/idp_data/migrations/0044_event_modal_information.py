# Generated by Django 2.2.10 on 2021-04-16 11:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idp_data', '0043_auto_20210416_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='modal_information',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Shown in modal but not on card.', null=True),
        ),
    ]
