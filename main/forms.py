from django.forms import ModelForm, TextInput
from .models import Film

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title']

        widgets = {
            "Title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Title"
            })
        }


class FilmRemarksForm(ModelForm):
    class Meta:
        model = Film
        fields = ['remark']

        widgets = {
            "Remark": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Remark"
            })
        }


class FilmOwnRatingForm(ModelForm):
    class Meta:
        model = Film
        fields = ['own_rating']

        widgets = {
            "Own rating": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Own rating"
            })
        }