from django.urls import path

from . import views

app_name='polls' #tells {% url 'polls:name' %} that polls points to this app, "Namespacing url names"
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"), #this is inserting the view defined under views.IndexView.as_view() instead of what we have defined under our views.py
    path('myindex/<int:pk>/', views.myIndexView.as_view(), name="myindex"),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'), #seems we are keeping our vote view
]