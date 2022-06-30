from django import forms
from .models import Contacto

class ContactoCreateForm(forms.ModelForm):
    class Meta:
        model=Contacto
        fields=('nombre','asunto','mail','mensaje')
