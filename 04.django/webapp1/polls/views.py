from django.shortcuts import render
from polls.models import Question, Choice

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    print(latest_question_list)

    context = {
        
        'name': '홍길동',
        'latest_question_list':latest_question_list
        
        
        }

    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    print('detail 함수 호출', question_id)
    pass

def vote(request, question_id):
    pass

def results(request, question_id):
    pass