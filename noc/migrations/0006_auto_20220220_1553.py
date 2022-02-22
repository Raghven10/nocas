# Generated by Django 3.2.6 on 2022-02-20 15:53

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('noc', '0005_auto_20220220_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='airport',
            field=models.ForeignKey(default=26625, on_delete=django.db.models.deletion.CASCADE, to='noc.airport'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='airport',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 20, 15, 53, 9, 946442, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='point',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noc.area'),
        ),
    ]