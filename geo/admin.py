from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Cities

@admin.register(Cities)
class LocationAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
    search_fields = ('name',)
