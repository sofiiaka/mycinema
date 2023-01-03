from django.forms import ModelForm, TextInput
from .models import Film

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['ukrainian_full_name']

        widgets = {
            "ukrainian_full_name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ukrainian full name"
            })
        }