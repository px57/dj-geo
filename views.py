from django.shortcuts import render
from django.db.models import Q

from kernel.http.decorators import load_response
from kernel.forms.default_forms import AutocompleteForm

from geo.rules.stack import GEO_RULESTACK
from geo.models import Countries, Cities, CitiesRelated, CountriesRelated
from geo.forms import SelectCityForm, SelectCountryForm


from kernel.http.exceptions import ExitResponse
import requests

import pycountry

@load_response(
    stack=GEO_RULESTACK,
    form=AutocompleteForm,
    json=True,
    load_params=True,
)
def find_city(
    request, 
    res=None,
    load_params=True,
    **kwargs
):
    """
    Find the country list and return the response.

    Args:
        request (Request): The request
        res (Response): The response
        **kwargs: The keyword arguments
    """
    _in = res.get_interface()
    dbCountry = []  # -> The list of countries to filter the cities.

    if _in.find_city_in_country:
        dbCountry = _in.find_city__getcountry()

    city_list = _in.find_city(
        query=request.form.cleaned_data['query'],
        country=dbCountry
    )
    res.city_list = [
        city.serialize(request) for city in city_list
    ]
    return res.success()

@load_response(
    stack=GEO_RULESTACK,
)
def selecteable_countries(
    request, 
    res=None, 
    **kwargs
):
    """
    Get the selecteable countries and return the response.
    """
    _in = res.get_interface()
    res.countries = []

    selecteable_countries = _in.selecteable_countries()
    query = Q()
    for country in selecteable_countries:
        query |= Q(code=country['code'])

    if len(query) == 0:
        return res.success()
    
    # -> country has in database, or create
    dbCountries = Countries.objects.filter(query)
    for country in selecteable_countries:
        dbCountry = dbCountries.filter(code=country['code']).first()
        if dbCountry is None:
            dbCountry = Countries(
                code=country['code']
            )
            dbCountry.save()

        res.countries.append(dbCountry.serialize(request))

    return res.success()

@load_response(
    stack=GEO_RULESTACK,
    form=SelectCountryForm,
    json=True,
)
def select_country(
    request, 
    res=None, 
    **kwargs
):
    """
    Select the country and return the response.
    """
    _in = res.get_interface()
    cleaned_data = request.form.cleaned_data

    countries_selected_max = _in.countries_selected_max
    if countries_selected_max is not None:
        dBcountries_selected = CountriesRelated.objects.filter(
            relatedModelId=cleaned_data['relatedModelId'],
            interface=_in.label,
        )
        if dBcountries_selected.count() >= countries_selected_max:
            return _in.event_max_countries_selected(dBcountries_selected)

    # -> Create the country related.
    dbCountriesSelected = CountriesRelated(
        interface=_in.label,
        country=cleaned_data['code'],
        relatedModelId=cleaned_data['relatedModelId'],
        relatedModel=cleaned_data['relatedModel']
    ).save()
    res.countries_selected = [dbCountriesSelected.serialize(request)]
    return res.success()

@load_response(stack=GEO_RULESTACK)
def select_city(
    request, 
    res=None, 
    **kwargs
):
    """
    Select the city and return the response.
    """
    _in = res.get_interface()

    return res.success()

