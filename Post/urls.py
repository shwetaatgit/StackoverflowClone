from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuestionList, name='home'),
    path('add_question/', views.addquestion, name="add_question"),
    path('<int:question_id>', views.Q_detail, name="detail"),
]