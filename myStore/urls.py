from django.urls import path
from . import views

urlpatterns = [
    path('all_books/', views.allBooks, name='all-books'),
    path('insert_book/', views.insertBook, name='insert-book'),
    path('get_book/<int:key>', views.getBook, name='get-book'),
    path('update_book/<int:key>', views.updateBook, name='update-book'),
    path('delete_book/<int:key>', views.deleteBook, name='delete-book'),

    path('', views.index),
    path('new/', views.new),
    path('home_page/', views.home_page, name='Home Page'),

]
