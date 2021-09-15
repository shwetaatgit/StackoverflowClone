from django import forms
from . import models

class AddQuestion(forms.ModelForm):
    class Meta:
        model = models.question
        fields = ['text']