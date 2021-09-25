from django import forms
from . import models

class AddQuestion(forms.ModelForm):
    class Meta:
        model = models.question
        fields = ['Que_text','tags']

class AddAnswer(forms.ModelForm):
    class Meta:
        model = models.answer
        fields = ['Ans_body']

class AddComment_Ques(forms.ModelForm):
    class Meta:
        model = models.comment
        fields = ['comment_text']

class AddComment_Ans(forms.ModelForm):
    class Meta:
        model = models.comment
        fields = ['comment_text']