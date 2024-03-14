
from django import forms

from geo.models import Countries, Cities

class CityValidator(forms.Field):
    """
        @description:
    """
    default_validators = []

    def __init__(self, load_bank_info=True, required=True):
        super().__init__()
        self.load_bank_info = load_bank_info
        self.required = required

    def to_python(self, city):
        """
            @description:
        """
        city = city.lower()
        return city
    
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
    