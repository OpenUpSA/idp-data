# Generated by Django 2.2.10 on 2020-09-03 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idp_data', '0023_municipality_homepage_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipality',
            name='by_laws_url',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]