from django.urls import path
from .views import *    # .으로 시작하면 현재 패키지를 의마함, .views --> 현재 패키지의 views 모듈

app_name = 'books'

urlpatterns = [

    # /books/
    path('',BooksModelView.as_view(), name='index'),

    # /books/book/
    path('book/',BookListView.as_view(), name='book_list'),

    # /books/book/99/
    path('book/<int:pk>/',BookDetailView.as_view(), name='book_detail'),

    # /books/publisher/
    path('publisher/',PublisherListView.as_view(), name='publisher_list'),

    # /books/publisher/99/
    path('publisher/<int:pk>/', PublisherDetailView.as_view(), name = 'publisher_detail'),

     # /books/author/
    path('author/',AuthorListView.as_view(), name='author_list'),

    # /books/author/99/
    path('author/<int:pk>/',AuthorDetailView.as_view(), name='author_detail'),

]