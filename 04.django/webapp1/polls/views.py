from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice
from django.urls import reverse

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    print(latest_question_list)

    context = {
        
        'name': '홍길동',
        'latest_question_list':latest_question_list
        
        
        }

    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # get() 한 행을 추출 할떄 사용,
    # 2행 이상이나, 없으면 예외가 발생
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def vote(request, question_id):
    # print('-'*80)
    # print('[headers]', request.headers)
    # print('[GET]', request.GET)     # request.GET['choice'], request.GET.get('choice')
    # print('[POST]', request.POST)   # request.POST['choice'], request.POST.get('choice')
    # print('[body]', request.body)   
    # print('-'*80)
    question = get_object_or_404(Question, pk=question_id)
    

    try:
        # .get(): 행이 2개 이상인 경우 또는 행이 없는 경우 예외 발생
        choice = request.POST['choice']
        selected_choice = question.choice_set.get(pk=choice)

    except:
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message': "You didn't select a choice.", 
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(
                    reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/results.html', {'question': question})