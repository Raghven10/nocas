# Generated by Django 3.2.6 on 2022-02-23 17:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('noc', '0013_alter_airport_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='waypoint',
            old_name='ats_route',
            new_name='atsroute',
        ),
        migrations.AlterField(
            model_name='airport',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 23, 17, 20, 31, 645600, tzinfo=utc)),
        ),
    ]
