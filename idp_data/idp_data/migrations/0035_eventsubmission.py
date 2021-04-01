# Generated by Django 2.2.10 on 2021-03-25 09:35

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('idp_data', '0034_auto_20210319_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission', ckeditor.fields.RichTextField()),
                ('submitter_name', models.CharField(max_length=255)),
                ('submitter_email', models.CharField(max_length=255)),
                ('submitted', models.DateField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='idp_data.Event')),
            ],
        ),
    ]