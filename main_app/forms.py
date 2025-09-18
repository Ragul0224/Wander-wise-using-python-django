from django import forms
from django.forms import ModelForm
from .models import Checking, VisitedPlace

class CheckingForm(ModelForm):
    class Meta:
        model = Checking
        fields = ['date']


# ✅ Moved outside the Meta class
class VisitedPlaceForm(forms.ModelForm):
    class Meta:
        model = VisitedPlace
        fields = ['name', 'description', 'image', 'visited_date']
