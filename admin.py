from django.contrib import admin

from geo import models

@admin.register(models.Countries)
class CountriesAdmin(admin.ModelAdmin):
    """
    The countries admin.
    """
    list_display = ('code',)

@admin.register(models.Cities)
class CitiesAdmin(admin.ModelAdmin):
    """
    The cities admin.
    """
    list_display = ('name', 'latitude', 'longitude', 'country',)

@admin.register(models.Languages)
class LanguagesAdmin(admin.ModelAdmin):
    """
    The languages admin.
    """
    list_display = ('name', 'country',)

@admin.register(models.CountriesRelated)
class CurrenciesAdmin(admin.ModelAdmin):
    """
    The currencies admin.
    """
    list_display = ('country',)

@admin.register(models.CitiesRelated)
class CitiesRelatedAdmin(admin.ModelAdmin):
    """
    The cities related admin.
    """
    list_display = ('city',)