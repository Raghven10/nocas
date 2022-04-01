from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Airport, AreaType, Obstruction, Area, Point, AtsRoute, RouteType, Waypoint

# Register your models here.

admin.site.register(Obstruction)

admin.site.register(Point)

admin.site.register(Area)

admin.site.register(AreaType)

admin.site.register(RouteType)
admin.site.register(AtsRoute)
admin.site.register(Waypoint)

# admin.site.register(Airport)
@admin.register(Airport)
class AirportAdmin(ImportExportModelAdmin):
    pass