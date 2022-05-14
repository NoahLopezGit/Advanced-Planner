import datetime

from django.db import models
from django.utils import timezone

#I believe the Question class inherits the models.Models attributes.
#This format defines a table (eg. 'Question' table) with Fields question_text 
# and pub_date, which are columns w/in this question table
#should be able to reference these columns with 'Question.question_text'
class Question(models.Model):
     #__str__ method represents the class object as a string 
     #invoke when print() or str() methods are used on the class itself
     def __str__(self): 
          return self.question_text


     def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

     question_text = models.CharField(max_length=200)
     #models.CharField is creating a character array (string) column under the name question_text
     #defined arguement max_length=200 is a way of defining characteristics of the question_text field
     pub_date = models.DateTimeField('date published')
     #can define name of the column like above

class Choice(models.Model):
     def __str__(self):
          return self.choice_text
     question = models.ForeignKey(Question, on_delete=models.CASCADE)
     #when choice is instantiated, it is created with a link to the specific question it answers
     #ForeignKey defines relationship with question
     #this one is telling django each choice is related to a single question??
     choice_text = models.CharField(max_length=200)
     #max_length is an example of an arguement required by CharField
     votes = models.IntegerField(default=0)
     #example setting default value of column

     #to activate the models:
     #include app in installed apps (polls app
     #Change your models (in models.py).
     #Run python manage.py makemigrations to create migrations for those changes
     #Run python manage.py migrate to apply those changes to the database.