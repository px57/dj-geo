from django.db import models
from django.forms.models import model_to_dict

from kernel.models.base_metadata_model import BaseMetadataModel
from kernel.models.fetch_all_models_file import choicesListRelatedModels

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
 
class CountriesRelated(BaseMetadataModel):
    """
    The countries related model.
    """
    interface = models.CharField(
        max_length=100,
        choices=GEO_RULESTACK.models_choices(),
    )

    country = models.ForeignKey(
        Countries,
        on_delete=models.CASCADE,
    )

    # -> Get the model object
    relatedModel = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        choices=choicesListRelatedModels()
    )

    # -> Get the nice object
    relatedModelId = models.IntegerField(
        null=True, 
        blank=True
    )

class CitiesRelated(BaseMetadataModel):
    """
    The countries related model.
    """
    interface = models.CharField(
        max_length=100,
        choices=GEO_RULESTACK.models_choices(),
    )

    city = models.ForeignKey(
        Cities,
        on_delete=models.CASCADE,
    )

    # -> Get the model object
    relatedModel = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        choices=choicesListRelatedModels()
    )

    # -> Get the nice object
    relatedModelId = models.IntegerField(
        null=True, 
        blank=True
    )