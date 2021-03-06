# Generated by Django 3.2.5 on 2021-10-07 15:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='NA', max_length=2000, verbose_name='name')),
                ('ident', models.CharField(default='NA', max_length=2000, verbose_name='ident')),
                ('type', models.CharField(default='NA', max_length=2000, verbose_name='type')),
                ('latitude_deg', models.FloatField(default=0.0, verbose_name='latitude_deg')),
                ('longitude_deg', models.FloatField(default=0.0, verbose_name='longitude_deg')),
                ('elevation_ft', models.FloatField(default=0.0, verbose_name='elevation_ft')),
                ('gps_code', models.CharField(default='NA', max_length=2000, verbose_name='gps_code')),
                ('iata_code', models.CharField(default='NA', max_length=2000, verbose_name='iata_code')),
                ('continent', models.CharField(default='NA', max_length=2000, verbose_name='continent')),
                ('country_name', models.CharField(default='NA', max_length=2000, verbose_name='country_name')),
                ('iso_country', models.CharField(default='NA', max_length=2000, verbose_name='iso_country')),
                ('region_name', models.CharField(default='NA', max_length=2000, verbose_name='region_name')),
                ('iso_region', models.CharField(default='NA', max_length=2000, verbose_name='iso_region')),
                ('local_region', models.CharField(default='NA', max_length=2000, verbose_name='local_region')),
                ('municipality', models.CharField(default='NA', max_length=2000, verbose_name='municipality')),
                ('scheduled_service', models.BooleanField(default=True, verbose_name='scheduled_service')),
                ('local_code', models.CharField(default='NA', max_length=215, verbose_name='local_code')),
                ('home_link', models.CharField(default='NA', max_length=2000, verbose_name='home_link')),
                ('wikipedia_link', models.CharField(default='NA', max_length=5000, verbose_name='wikipedia_link')),
                ('keywords', models.CharField(default='NA', max_length=5000, verbose_name='keywords')),
                ('score', models.IntegerField(default=0, verbose_name='score')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2021, 10, 7, 15, 53, 23, 283215, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Obstruction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(default=0.0, max_length=7)),
                ('longitude', models.FloatField(default=0.0, max_length=7)),
                ('height', models.FloatField(default=0.0, max_length=7)),
                ('site_elevation', models.FloatField(default=0.0, max_length=7)),
            ],
        ),
    ]
