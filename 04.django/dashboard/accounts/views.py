from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class UserCreateView(generic.CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm

    # 회원가입 성공시 이동할 url 지정
    success_url = reverse_lazy('accounts:register_done')



class UserCreateDoneView(generic.TemplateView):
    template_name = 'registration/register_done.html'

