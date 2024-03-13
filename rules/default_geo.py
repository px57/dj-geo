
from django.conf import settings

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