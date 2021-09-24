from django.db import models
from django.contrib.auth.models import User
from django.utils import tree

class question(models.Model):
    Que_text = models.TextField()
    Que_author = models.ForeignKey(User, on_delete= models.CASCADE)
    Que_created_on = models.DateTimeField(auto_now_add=True)
    Upvotes_Que = models.ManyToManyField(User,related_name = 'Qupvotes', null=True, blank=True)
    Views = models.ManyToManyField(User,related_name = 'Qviews', null=True, blank=True)

    def total_upvotes(self):
        return self.Upvotes_Que.count()

    def total_views(self):
        return self.Views.count()

    class Meta:
        ordering = ['-Que_created_on']

    def __str__(self):
        return self.Que_text

class answer(models.Model):
    question = models.ForeignKey(question, related_name= 'answers', on_delete= models.CASCADE)
    Ans_body = models.TextField()
    Ans_author = models.ForeignKey(User, on_delete= models.CASCADE)
    Ans_created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-Ans_created_on']

    def __str__(self):
        return '%s - %s' % (self.question.Que_text, self.Ans_author)

class comment(models.Model):
    question = models.ForeignKey(question, related_name= 'comments',on_delete= models.CASCADE, null=True)
    answer = models.ForeignKey(answer,  related_name= 'comments_ans',on_delete= models.CASCADE, null=True)
    comment_text = models.TextField()
    comment_author = models.ForeignKey(User, on_delete= models.CASCADE)
    comment_created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_created_on']

    def __str__(self):
        return '%s - %s' % (self.comment_text, self.comment_author)