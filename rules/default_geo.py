


from django.utils import timezone
import os
from geo.rules.stack import GEO_RULESTACK
from kernel.interfaces.interfaces import InterfaceManager
import PIL

class DefaultRuleClass(InterfaceManager):
    """
    The default rule class. 
    """

