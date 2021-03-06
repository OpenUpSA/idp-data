# Generated by Django 2.2.10 on 2021-03-04 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idp_data', '0030_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(default='', help_text='This is shown to users.', max_length=1000),
        ),
        migrations.AlterField(
            model_name='event',
            name='short_desc',
            field=models.TextField(help_text='Max. 500 characters', max_length=500),
        ),
    ]
