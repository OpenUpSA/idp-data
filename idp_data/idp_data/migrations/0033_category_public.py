# Generated by Django 2.2.10 on 2021-03-19 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idp_data', '0032_municipality_financial_performance_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='public',
            field=models.BooleanField(default=False, help_text='Whether this category is a public or internal event'),
        ),
    ]
