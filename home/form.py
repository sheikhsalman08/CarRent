from django import forms
from .models import Car

class SearchForm(forms.ModelForm):
   class Meta:
      model = Car
      fields = ['address','model']
