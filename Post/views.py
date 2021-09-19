from django.shortcuts import get_object_or_404, render,redirect
from .models import answer, question
from . import forms
import Post

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
            instance.Que_author = request.user
            instance.save()
            return redirect('home')
    else:
        form= forms.AddQuestion()
    return render(request, 'AddQuestion.html',{'form':form})

def Q_detail(request, question_id):
    obj = get_object_or_404(question, pk=question_id)
    if request.method=='POST':
        form= forms.AddAnswer(request.POST, request.FILES)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.Ans_author = request.user
            instance.question = question.objects.get(pk=question_id)
            instance.save()
            return redirect('home')
    else:
        form= forms.AddAnswer()
    return render(request, 'detail.html',{'obj':obj,'form':form})