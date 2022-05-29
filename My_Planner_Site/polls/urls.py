from django.urls import path

from . import views

app_name='polls' #tells {% url 'polls:name' %} that polls points to this app, "Namespacing url names"
urlpatterns = [
    path('index/', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('myview/',views.myview, name='myview') #what is the name doing
]