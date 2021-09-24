from django.shortcuts import get_object_or_404, render,redirect
from .models import answer, question, comment
from . import forms
import Post

def QuestionList(request):
    questions = question.objects.all()
    context ={
        'question_list': questions,
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

def addcomment_ques(request, question_id):
    if request.method=='POST':
        form= forms.AddComment_Ques(request.POST)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.comment_author = request.user
            instance.question = question.objects.get(pk=question_id)
            instance.save()
            return redirect('home')
    else:
        form= forms.AddComment_Ques()
    return render(request, 'AddComment.html',{'form':form})

def addcomment_ans(request, answer_id):
    if request.method=='POST':
        form= forms.AddComment_Ans(request.POST)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.comment_author = request.user
            instance.answer = answer.objects.get(pk=answer_id)
            instance.save()
            return redirect('home')
    else:
        form= forms.AddComment_Ans()
    return render(request, 'AddComment.html',{'form':form})

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
        
    context={
        'obj':obj,
        'form': form
    }
    return render(request, 'detail.html',context)