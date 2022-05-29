from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


#notice default views are generated with classes, wheras our custom views are defined under functions
class IndexView(generic.ListView): #IndexView is inheriting attributes of generic.ListView
    template_name = 'polls/index.html' #does this not have a default template it looks for ?
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView): 
    #if this i not specified it will look for template under name of <app name>/<model name>_detail.html; so polls/question_detail.html
    #presumably under the templates directory in polls
    model = Question 
    #template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'





def vote(request, question_id):
    ... # same as above, no changes needed.