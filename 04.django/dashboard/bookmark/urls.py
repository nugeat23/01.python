from django.urls import path
from bookmark.views import *

app_name = 'bookmark'

urlpatterns = [


    path('',BookmarkListView.as_view(), name='index'),
    path('<int:pk>/', BookmarkDetailView.as_view(), name='detail'),

    # Example: /bookmark/add/
    path('add/', BookmarkCreateView.as_view(), name='add'),





]