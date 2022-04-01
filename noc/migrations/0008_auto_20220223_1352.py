# Generated by Django 3.2.6 on 2022-02-23 13:52

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('noc', '0007_auto_20220222_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('upper_limit', models.IntegerField()),
                ('lower_limit', models.IntegerField()),
                ('lateral_limit', models.IntegerField()),
                ('mfa', models.IntegerField()),
                ('color', models.CharField(default='black', max_length=50)),
                ('description', models.CharField(default='black', max_length=50, null=True)),
                ('reference', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RouteType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
        migrations.AlterField(
            model_name='airport',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 23, 13, 52, 50, 602661, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='point',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='noc.area'),
        ),
        migrations.CreateModel(
            name='Waypoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
                ('route', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='noc.route')),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='route_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noc.routetype'),
        ),
    ]
