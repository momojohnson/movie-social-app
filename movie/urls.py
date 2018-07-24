from django.contrib import admin
from django.urls import path
from movie import views
app_name = 'movies'
urlpatterns = [
    path('movies/', views.MoviesListPageView.as_view(), name='movies_list'),
    path('movies/<slug:movie_slug>-<int:movie_id>/', views.MovieDetailsPageView.as_view(), name='movie_details')
]
