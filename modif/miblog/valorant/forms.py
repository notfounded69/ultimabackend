from django import forms
from .models import formBD

class ValidacionForm(forms.ModelForm):
    class Meta:
        model= formBD
        fields = ['nombre','correo']
        
    