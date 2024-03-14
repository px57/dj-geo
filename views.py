from django.shortcuts import render
from django.db.models import Q

from kernel.http.decorators import load_response
from kernel.forms.default_forms import AutocompleteForm

from geo.rules.stack import GEO_RULESTACK
from geo.models import Countries, Cities, CitiesRelated, CountriesRelated
from geo.forms import SelectCityForm, SelectCountryForm

import pycountry

@load_response(
    stack=GEO_RULESTACK,
    form=AutocompleteForm,
    json=True,
)
def find_city(request, res=None):
    """
    Find the country list and return the response.
    """
    _in = res.get_interface()
    # -> Call the service to get the autocomplete list
    # -> Save the list of cities in the response
    # -> return serialized response
    return res.success()

@load_response(
    stack=GEO_RULESTACK,
)
def selecteable_countries(request, res=None):
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
    load_params=True
)
def select_country(request, res=None):
    """
    Select the country and return the response.
    """
    _in = res.get_interface()
    cleaned_data = request.form.cleaned_data
    print (cleaned_data)
    # dbCitiesRelated = CitiesRelated(
    #     country=cleaned_data['code'],
    #     relatedModelId=cleaned_data['relatedModelId'],
    #     relatedModel=cleaned_data['relatedModel']
    # ).save()
    return res.success()

@load_response(stack=GEO_RULESTACK)
def select_city(request, res=None):
    """
    Select the city and return the response.
    """
    _in = res.get_interface()

    return res.success()

