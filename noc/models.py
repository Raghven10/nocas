import django.utils.timezone
from django.db import models

class Airport(models.Model):
    name = models.CharField(("name"), max_length=2000, default="NA")
    ident = models.CharField(("ident"), max_length=2000, default="NA")
    type = models.CharField(("type"), max_length=2000, default="NA")
    latitude_deg = models.FloatField(("latitude_deg"),  default=0.0)
    longitude_deg = models.FloatField(("longitude_deg"),  default=0.0)
    elevation_ft = models.FloatField(("elevation_ft"), default=0.0)
    gps_code = models.CharField(("gps_code"), max_length=2000, default="NA")
    iata_code = models.CharField(("iata_code"), max_length=2000, default="NA")
    continent = models.CharField(("continent"), max_length=2000, default="NA")
    country_name = models.CharField(("country_name"), max_length=2000, default="NA")
    iso_country = models.CharField(("iso_country"), max_length=2000, default="NA")
    region_name = models.CharField(("region_name"), max_length=2000, default="NA")
    iso_region = models.CharField(("iso_region"), max_length=2000, default="NA")
    local_region = models.CharField(("local_region"), max_length=2000, default="NA")
    municipality = models.CharField(("municipality"), max_length=2000, default="NA")
    scheduled_service = models.BooleanField(("scheduled_service"), default=True)
    local_code = models.CharField(("local_code"), max_length=215, default="NA")
    home_link = models.CharField(("home_link"), max_length=2000, default="NA")
    wikipedia_link = models.CharField(("wikipedia_link"), max_length=5000, default="NA")
    keywords = models.CharField(("keywords"), max_length=5000, default="NA")
    score = models.IntegerField(("score"), default=0)
    pub_date = models.DateTimeField(default=django.utils.timezone.now())

class Obstruction(models.Model):
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    height = models.FloatField(default=0.0)
    site_elevation = models.FloatField(default=0.0)

class Area(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=50, default='black')
    fill_color = models.CharField(max_length=50, default='orange')  
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)


class Point(models.Model):
    point_name = models.CharField(max_length=200)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    

