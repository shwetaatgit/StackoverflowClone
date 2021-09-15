from django.db import models
from django.contrib.auth.models import User

class question(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.text