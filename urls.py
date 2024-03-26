"""
    @description: This file contains the urls for the profiles app
"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        'select_country/', 
        views.select_country, 
        name='geo__select_country'
    ),
    path(
        'find_city/',
        views.find_city,
        name='geo__find_city'
    ),
    path(
        'select_city/',
        views.select_city,
        name='geo__select_city'
    ),
    path(
        'selecteable_countries/',
        views.selecteable_countries,
        name='geo__selecteable_countries'
    ),
]