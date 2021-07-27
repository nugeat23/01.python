from django.urls import path
from polls import views

app_name = 'polls'

urlpatterns =[
    # /polls/
    path('', views.index, name='index'),
    # /polls/1
    path('<int:question_id>/detail/', views.detail, name='detail'),

    # /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),

]