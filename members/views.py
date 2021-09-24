from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def Register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form.save
        return redirect('login')

    return render(request, "registration/register.html", {'form': form})
