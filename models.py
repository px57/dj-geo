from django.db import models
from django.forms.models import model_to_dict

from kernel.models.base_metadata_model import BaseMetadataModel

from geo.rules.stack import GEO_RULESTACK

import pycountry

class Countries(BaseMetadataModel):
    """
    The countries model.
    """
    code = models.CharField(
        max_length=10,
        choices=GEO_RULESTACK.rules_choices('selecteable_countries'),
        unique=True,
    )

    class Meta:
        """
        The meta class.
        """
        db_table = 'countries'
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.code
        
class Cities(BaseMetadataModel):
    """
    The cities model.
    """
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
    )

    name = models.CharField(
        max_length=100,
    )

    country = models.ForeignKey(
        Countries,
        on_delete=models.CASCADE,
    )

    class Meta:
        """
        The meta class.
        """
        db_table = 'cities'
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name
    
class Languages(BaseMetadataModel):
    """
    The languages model.
    """
    country = models.ForeignKey(
        Countries,
        on_delete=models.CASCADE,
    )
    
    name = models.CharField(
        max_length=100,
        choices=(

        ),
    )
 