from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.Register, name = 'register'),
]