
from django.conf import settings

# from kernel.http import Response
from kernel.interfaces.interfaces import InterfaceManager

import pycountry

class DefaultRuleClass(InterfaceManager):
    """
    The default rule class. 
    """

    """
    Is the service mail to be used.
    """
    service = settings.GEO_SERVICE

    """
    The service configuration name.
    """
    service_config_name = 'GOOGLEMAP'

    """
    Settings config name.
    """
    settings_config_name = 'GEO_CONFIG_AUTHENTIFICATION_KEYS'

    """
    Service module.
    """
    service_module = 'geo.__services__'

    """
    The selecteable countries code list.

    Choices:
        ['AF', 'AX', 'AL'] -> Afghanistan, Aland Islands, Albania
        '*' -> All countries
    """
    selecteable_countries_code_list = '*'

    def get_all_countries(self):
        """
        Get all countries.
        """
        result = []
        for country in pycountry.countries:
            result.append({
                'code': country.alpha_2,
                'name': country.name,
            })
        return result

    def selecteable_countries(self):
        """
        Get the selecteable countries.
        """
        if '*' in self.selecteable_countries_code_list:
            return self.get_all_countries()
        elif type(self.selecteable_countries_code_list) is str:
            raise ValueError('The selecteable_countries_code_list must be a list.')

        result = []
        for country in self.get_all_countries():
            if country['code'] in self.selecteable_countries_code_list:
                result.append(country)
        return result

    def selecteable_countries__rules_choices(self, choices: list):
        """
        Get the selecteable countries rules choices.
        """
        for country in self.selecteable_countries():
            choices.append((country['code'], country['name']))
        
        return choices
    
    # **************************** [Countries] ****************************
    """
    The maximum number of countries selected, in the CountriesRelated model.

    Choices:
        (int) -> The maximum number of countries selected
        (None) -> No limit
    """
    countries_selected_max = 1

    def event_max_countries_selected(self, dBcountries_selected):
        """
        Event when the maximum number of countries selected is reached.
        """
        cleaned_data = self.request.form.cleaned_data
        dBcountries_selected.update(        
            country=cleaned_data['code'],
            relatedModelId=cleaned_data['relatedModelId'],
            relatedModel=cleaned_data['relatedModel']
        )
        self.res.countries_selected = [
            country.serialize(self.request) for country in dBcountries_selected
        ]
        return self.res.success()
    
    # **************************** [Find Cities] ****************************
    """
    Activate the find city in country.
    """
    find_city_in_country = False

    def find_city__getcountry(self):
        """
        Get the country.
        """
        if self.request.POST.get('country') is None:
            raise ValueError('The request.POST[\'country_code\'] is required.')
        
        from geo.models import Countries, CountriesRelated
        country_code = self.request.POST.get('country')
        if type(country_code) is str:
            dbCountry = Countries.objects.filter(code=country_code).first()
            if dbCountry is None:
                raise ValueError('The country code not found, in the database.')
            return dbCountry
        elif type(country_code) is CountriesRelated:
            return [country_code.country]
        elif type(country_code) is Countries:
            return [country_code]

    def find_city(self, *args, **kwargs):
        """
        Find the country list and return the response.
        """
        self.gpm_service.set_config(self)
        return self.gpm_service.find_city(*args, **kwargs)