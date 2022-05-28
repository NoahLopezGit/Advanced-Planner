
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http import HttpResponse
# Create your views here.



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request,'polls/index.html', context) #why does this method need the request object?


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #pk is primary key, question unique identifier
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def myview(request): #for some reason you must pass request to this function
    return HttpResponse("myview")


# Leave the rest of the views (detail, results, vote) unchanged