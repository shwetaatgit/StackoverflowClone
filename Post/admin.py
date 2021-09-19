from django.contrib import admin

# Register your models here.
from .models import question, answer

admin.site.register(question)
admin.site.register(answer)