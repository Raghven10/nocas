from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

# Register your models here.


from .models import Airport, Obstruction

# admin.site.register(Airport)
admin.site.register(Obstruction)

@admin.register(Airport)
class AirportAdmin(ImportExportModelAdmin):
    pass