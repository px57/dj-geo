from django.shortcuts import render

from kernel.http.decorators import load_response

from geo.rules.stack import GEO_RULESTACK

@load_response(stack=GEO_RULESTACK)
def find_city(request, res=None):
    """
    Find the country list and return the response.
    """
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
    return res.success()

