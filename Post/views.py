from django.shortcuts import get_object_or_404, render,redirect, HttpResponse
from .models import answer, question, comment
from . import forms
import Post
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import UpdateView
from .forms import EditForm
from django.urls import reverse_lazy

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
            return HttpResponseRedirect(reverse('detail',args=[str(question_id)]))
    else:
        form= forms.AddComment_Ques()
    return render(request, 'AddComment.html',{'form':form})

def addcomment_ans(request, answer_id,question_id):
    if request.method=='POST':
        form= forms.AddComment_Ans(request.POST)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.comment_author = request.user
            instance.answer = answer.objects.get(pk=answer_id)
            instance.save()
            return HttpResponseRedirect(reverse('detail',args=[str(question_id)]))
    else:
        form= forms.AddComment_Ans()
    return render(request, 'AddComment_A.html',{'form':form})

def Q_detail(request, question_id):
    obj = get_object_or_404(question, pk=question_id)
    if  request.user.is_authenticated:
        obj.Views.add(request.user)
    # if obj.Views.filter(id=request.user.id).exists():
    #     obj.Views.add(request.user)
        
    is_up = False
    if obj.Upvotes_Que.filter(id=request.user.id).exists():
        is_up = True
        
    if request.method=='POST':
        form= forms.AddAnswer(request.POST, request.FILES)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.Ans_author = request.user
            instance.question = question.objects.get(pk=question_id)
            instance.save()
            return HttpResponseRedirect(reverse('detail',args=[str(question_id)]))
    else:
        form= forms.AddAnswer()
    
    context={
        'obj':obj,
        'form': form,
        'is_up': is_up,
        'total_upvotes':obj.total_upvotes(),
        'total_views':obj.total_views(),
    }
    return render(request, 'detail.html',context)

def Upvote(request, question_id):
    obj = get_object_or_404(question, pk=question_id)
    is_up = False
    if obj.Upvotes_Que.filter(id=request.user.id).exists():
        obj.Upvotes_Que.remove(request.user)
        is_up = False
    else:
        obj.Upvotes_Que.add(request.user)
        is_up = True
    return HttpResponseRedirect(reverse('detail',args=[str(question_id)]))

def search(request):
    query = request.GET['query']
    if len(query)>80:
        questions = []
    else:
        questions = question.objects.filter(tags__icontains=query)
    context ={
        'question_list': questions,
    }
    return render(request, "search.html", context)

def editquestion(request, question_id):
    ques = get_object_or_404(question, pk=question_id)
    
    if request.method=='POST':
        form= forms.EditForm(request.POST,instance=ques)
        
        if form.is_valid():
            instance= form.save(commit=False)
            if instance.Que_author == request.user:
                instance.save()
            return HttpResponseRedirect(reverse('detail',args=[str(question_id)]))
    else:
        form= forms.EditForm(instance=ques)
    return render(request, 'EditQues.html',{'form':form, 'ques':ques})

def editcomment(request,comment_id, question_id):
    comm = get_object_or_404(comment, pk=comment_id)

    if request.method=='POST':
        form= forms.EditComment(request.POST,instance=comm)
        if form.is_valid():
            instance= form.save(commit=False)
            if instance.comment_author == request.user:
                instance.save()
            return HttpResponseRedirect(reverse('detail',args=[str(question_id)]))
    else:
        form= forms.EditComment(instance=comm)
    return render(request, 'EditComment.html',{'form':form, 'comm':comm})

def editanswer(request,answer_id, question_id):
    ans = get_object_or_404(answer, pk=answer_id)

    if request.method=='POST':
        form= forms.AddAnswer(request.POST,instance=ans)
        if form.is_valid():
            instance= form.save(commit=False)
            if instance.Ans_author == request.user:
                instance.save()
            return HttpResponseRedirect(reverse('detail',args=[str(question_id)]))
    else:
        form= forms.AddAnswer(instance=ans)
    return render(request, 'EditAns.html',{'form':form, 'ans':ans})
