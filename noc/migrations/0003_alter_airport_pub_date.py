# Generated by Django 3.2.5 on 2021-10-07 15:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('noc', '0002_alter_airport_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 7, 15, 55, 24, 938771, tzinfo=utc)),
        ),
    ]