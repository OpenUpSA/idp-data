# Generated by Django 2.2.10 on 2020-08-23 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idp_data', '0013_auto_20200823_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.DateField(default='2020-08-22'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateField(blank=True, default='2020-08-22'),
            preserve_default=False,
        ),
    ]
