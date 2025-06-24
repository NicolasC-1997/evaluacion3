from django import forms
from .models import Reclamo

class ReclamoForm(forms.ModelForm):
    class Meta:
        model = Reclamo
        fields = '__all__'
