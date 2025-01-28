from django.urls import path
from .views import BookListCreateView
from . import views


urlpatterns= [
    path('', BookListCreateView.as_view()),
    path('books/', views.book_list,name='book-list'),
]