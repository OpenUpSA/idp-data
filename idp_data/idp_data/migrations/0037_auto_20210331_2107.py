# Generated by Django 2.2.10 on 2021-03-31 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idp_data', '0036_auto_20210325_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventsubmission',
            old_name='submitter_email',
            new_name='submitter_contact',
        ),
        migrations.AlterField(
            model_name='eventsubmission',
            name='submitted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
