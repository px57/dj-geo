from django.contrib import admin

from geo import models

@admin.register(models.Countries)
class CountriesAdmin(admin.ModelAdmin):
    """
    The countries admin.
    """
    list_display = ('name', 'code',)

@admin.register(models.Cities)
class CitiesAdmin(admin.ModelAdmin):
    """
    The cities admin.
    """
    list_display = ('name', 'latitude', 'longitude', 'country',)

    