from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question


#notice default views are generated with classes, wheras our custom views are defined under functions
class myIndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.



class IndexView(generic.ListView): #IndexView is inheriting attributes of generic.ListView
    template_name = 'polls/index.html' #default is  <app name>/<model name>_list.html
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView): 
    #if this i not specified it will look for template under name of <app name>/<model name>_detail.html; so polls/question_detail.html
    #presumably under the templates directory in polls
    context_object_name = "myQuestion" 

    #poll/urls.py says value in url is PK, will be used automatically to find question with associated PK
    #model= Question specifies what table for PK to be used with. Once handler has grabbed our question and loaded it to the question model
    #it can be accessed and modified directly by the html template under the default given name or whatever we specify in 
    #context_object_name
    model = Question 
    #template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button. why?
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) #it seems this has more complex handing than just positional logic
