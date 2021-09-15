from django.shortcuts import get_object_or_404, render,redirect
from .models import question
from . import forms

def QuestionList(request):
    questions = question.objects.all()
    context ={
        'question_list': questions
    }
    return render(request, "home.html", context)

def addquestion(request):
    if request.method=='POST':
        form= forms.AddQuestion(request.POST, request.FILES)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('home')
    else:
        form= forms.AddQuestion()
    return render(request, 'AddQuestion.html',{'form':form})

def Q_detail(request, id):
    obj= get_object_or_404(question,pk=id)
    return render(request,'detail.html',{'obj':obj})