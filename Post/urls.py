from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuestionList, name='home'),
    path('add_question/', views.addquestion, name="add_question"),
    path('search/', views.search, name="search"),
    path('add_comment/<int:question_id>', views.addcomment_ques, name="add_comment_Q"),
    path('add_comment/<int:question_id>/<int:answer_id>', views.addcomment_ans, name="add_comment_A"),
    path('<int:question_id>', views.Q_detail, name="detail"),
    path('upvote/<int:question_id>', views.Upvote, name="upvote"),
]