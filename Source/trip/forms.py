from django.forms import ModelForm

from .models import *

class Spot_form(ModelForm):

    class Meta:

        model=HiddenSpot

        fields='__all__'
