# Generated by Django 3.2.6 on 2022-02-23 15:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('noc', '0008_auto_20220223_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 23, 15, 54, 25, 972053, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='route',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
