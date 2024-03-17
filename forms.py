
from django import forms

from geo import validators

from kernel.forms.validators import RelatedModelValidator

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
    code = validators.CountryValidator(
        required=True,
    )
    
    relatedModelId = forms.IntegerField(
        required=True
    )

    relatedModel = RelatedModelValidator(
        required=True
    )

class SelectCityForm(forms.Form):
    """
    Form to select a city.
    """
    city_id = validators.CityValidator(
        required=True
    )

    relatedModelId = forms.IntegerField(
        required=True
    )

    relatedModel = RelatedModelValidator(
        required=True
    )