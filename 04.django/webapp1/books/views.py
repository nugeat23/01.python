from django.shortcuts import render
from django.views import generic
from books.models import *


# 모델(db) 연동없이 html 템플릿만 처리하는 경우
# TemplateView 사용
class BooksModelView(generic.TemplateView):
    template_name = 'books/index.html'  # html 탬플릿 파일 경로

    # get_context_data() 오버라이드(override)
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)    # 부모의 디폴트 호출
        context['model_list'] = [
            # 'Book', 'Author', 'Publisher'
            ('Books', 'books:book_list'), 
            ('Author', 'books:author_list'),
            ('Publisher', 'books:publisher_list')           
                        
            ]
        
        return context

# Book 모델의 목록을 보여주는 뷰
class BookListView(generic.ListView):

    model = Book
    context_object_name = 'book_list' # object_list -> book_list

class BookDetailView(generic.DetailView):

    model = Book


class PublisherListView(generic.ListView):
    model = Publisher

class PublisherDetailView(generic.DetailView):
    model = Publisher

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author