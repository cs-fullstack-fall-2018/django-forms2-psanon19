from django import forms
from .models import FormModel


class PostForm(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = {'name', 'dateCreated', }
