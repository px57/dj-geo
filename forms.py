
from django import forms

from geo import validators


class SelectCityForm(forms.Form):
    """
    Form to select a city.
    """
    city = validators.CityValidator(
        required=True
    )

class SelectCountryForm(forms.Form):
    """
    Form to select a country.
    """
    country = validators.CountryValidator(
        required=True
    )

