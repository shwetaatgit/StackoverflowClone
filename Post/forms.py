from django import forms
from . import models

class AddQuestion(forms.ModelForm):
    class Meta:
        model = models.question
        fields = ['Que_text']

class AddAnswer(forms.ModelForm):
    class Meta:
        model = models.answer
        fields = ['Ans_body']