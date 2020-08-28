# Generated by Django 2.2.10 on 2020-08-18 20:56

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('idp_data', '0008_auto_20200816_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipality',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventaction',
            name='event',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='actions', to='idp_data.Event'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventaction',
            name='raw_html',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
