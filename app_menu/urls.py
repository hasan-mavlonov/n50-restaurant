from django.urls import path
from app_menu import views

app_name = 'app_menu'

urlpatterns = [
    path('authors/', views.author_list_create, name='author-list-create'),
    path('books/', views.book_list_create, name='book-list-create'),
]



