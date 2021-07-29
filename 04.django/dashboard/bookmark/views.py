from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from bookmark.models import Bookmark
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class BookmarkListView(ListView):
    model = Bookmark

class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url']   # form 클래스에서 사용할 필드 ->form 클래스 자동생성
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form): # post 요청시 form의 유효성 검사 통과되면 호출
        # form.instance : 폼 정보를 기반으로 생성된 모델 인스턴스
        form.instance.owner = self.request.user # 로그인 사용자 정보

        return super().form_valid(form)     # 모델 인스턴스 저장