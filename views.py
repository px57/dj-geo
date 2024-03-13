from django.shortcuts import render

from kernel.http.decorators import load_response
from kernel.forms.default_forms import AutocompleteForm

from geo.rules.stack import GEO_RULESTACK
from geo.models import Countries, Cities

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
    
    return res.success()

@load_response(stack=GEO_RULESTACK)
def selecteable_countries(request, res=None):
    """
    Get the selecteable countries and return the response.
    """
    _in = res.get_interface()
    return res.success()

@load_response(stack=GEO_RULESTACK)
def select_country(request, res=None):
    """
    Select the country and return the response.
    """
    return res.success()

@load_response(stack=GEO_RULESTACK)
def select_city(request, res=None):
    """
    Select the city and return the response.
    """
    _in = res.get_interface()

    return res.success()

