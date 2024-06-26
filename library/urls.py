from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('add_book/', views.add_book, name='add_book'),
    path('update_book/<int:pk>/', views.update_book, name='update_book'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_category/', views.add_category, name='add_category'),
]


