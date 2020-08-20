# Generated by Django 2.2.10 on 2020-08-19 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('idp_data', '0009_auto_20200818_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostnameMunicipality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=200)),
                ('muni', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='idp_data.Municipality')),
            ],
        ),
    ]
