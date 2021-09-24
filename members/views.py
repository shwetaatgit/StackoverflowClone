from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def Register(request):
    if request.method == 'POST':
    	form = UserCreationForm(request.POST)
    	if form.is_valid():
    		form.save()
    		return redirect('login')
    else:
    	form = UserCreationForm()

    return render(request, "registration/register.html", {'form': form})
