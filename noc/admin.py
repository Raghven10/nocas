from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Airport, Obstruction, Area, Point

# Register your models here.

admin.site.register(Obstruction)

admin.site.register(Point)

admin.site.register(Area)


# admin.site.register(Airport)
@admin.register(Airport)
class AirportAdmin(ImportExportModelAdmin):
    pass