from django.db import models

#I believe the Question class inherits the models.Models attributes.
#This format defines a table (eg. 'Question' table) with Fields question_text 
# and pub_date, which are columns w/in this question table
#should be able to reference these columns with 'Question.question_text'
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    #models.CharField is creating a character array (string) column under the name question_text
    #defined arguement max_length=200 is a way of defining characteristics of the question_text field
    pub_date = models.DateTimeField('date published')
    #can define name of the column like above

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
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