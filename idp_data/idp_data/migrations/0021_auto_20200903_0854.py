# Generated by Django 2.2.10 on 2020-09-03 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idp_data', '0020_municipalityhostname_homepageurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='municipalityhostname',
            name='homepageURL',
        ),
        migrations.AddField(
            model_name='municipality',
            name='homepageURL',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
