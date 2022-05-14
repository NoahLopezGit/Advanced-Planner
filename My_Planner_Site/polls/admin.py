from django.contrib import admin

# Register your models here.
from .models import Question, Choice #.models?

admin.site.register(Question) #this gives access to question model on admin site
admin.site.register(Choice)