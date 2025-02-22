# planner/forms.py
from django import forms
from .models import Place

class TravelForm(forms.Form):
    places = forms.ModelMultipleChoiceField(queryset=Place.objects.all())
class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'description']