# Generated by Django 2.2.10 on 2020-11-25 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idp_data', '0026_auto_20201111_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipality',
            name='page_title',
            field=models.CharField(default='Public Participation Guide', max_length=200),
        ),
    ]