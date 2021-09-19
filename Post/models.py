from django.db import models
from django.contrib.auth.models import User

class question(models.Model):
    Que_text = models.TextField()
    Que_author = models.ForeignKey(User, on_delete= models.CASCADE)
    Que_created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-Que_created_on']

    def __str__(self):
        return self.text

class answer(models.Model):
    question = models.ForeignKey(question, related_name= 'answers', on_delete= models.CASCADE)
    Ans_body = models.TextField()
    Ans_author = models.ForeignKey(User, on_delete= models.CASCADE)
    Ans_created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-Ans_created_on']

    def __str__(self):
        return '%s - %s' % (self.question.text, self.author)