
from django import forms

from geo.models import Countries, Cities

class CityValidator(forms.Field):
    """
        @description:
    """
    default_validators = []

    def __init__(self, required=True):
        super().__init__()
        self.required = required

    def to_python(self, city_id):
        """
            @description:
        """
        dbCity = Cities.objects.filter(id=city_id).first()
        if dbCity is None:
            raise forms.ValidationError('City not found')
        return dbCity
    
class CountryValidator(forms.Field):
    """
        @description:
    """
    default_validators = []

    def __init__(
            self, 
            required=True
    ):
        super().__init__()
        self.required = required

    def to_python(self, country):
        """
            @description:
        """
        country = country.upper()
        dbCountry = Countries.objects.filter(code=country).first()
        if dbCountry is None:
            raise forms.ValidationError('Country not found')
        return dbCountry