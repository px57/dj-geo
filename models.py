from django.db import models
from django.forms.models import model_to_dict

from gpm.models.base_metadata_model import BaseMetadataModel
from gpm.models.fetch_all_models_file import choicesListRelatedModels

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

class DiplomaticZone(BaseMetadataModel):
    """
    The states model.
    """

    """
    The diplomatic zone model.

    Example:
        0 -> Is states in USA
        But 
        0 -> Is an region in France
    """
    depth = models.IntegerField(
        default=0,
        help_text='The depth of the zone in the country',
    )

    country = models.ForeignKey(
        Countries,
        on_delete=models.CASCADE,
        help_text='The country of the zone',
    )

    zone_parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text='The parent zone',
    )

    name = models.CharField(
        max_length=100,
        help_text='The name of the zone',
    )



class Cities(BaseMetadataModel):
    """
    The cities model.
    """
    reference_code = models.CharField(
        max_length=250,
        unique=True,
        default='',
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        default=0,
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        default=0,
    )

    name = models.CharField(
        max_length=100,
    )

    country = models.ForeignKey(
        Countries,
        on_delete=models.CASCADE,
    )

    api_data = models.JSONField(
        null=True,
        blank=True,
        default=dict,
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
    
    def serialize(self, request):
        serialize = super().serialize(request)
        del serialize['api_data']
        del serialize['reference_code']
        serialize['country'] = self.country.serialize(request)
        return serialize
    
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