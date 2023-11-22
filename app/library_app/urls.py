from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('genre/<slug:slug>/', views.GenreDetail.as_view(), name='genre'),
    path('search/', views.SearchResult.as_view(), name='search')
]

