from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from movie.models import NowPlayingMovie


class MoviesListPageView(ListView):
    """ Handles the listing of all movies route /movies"""
    model = NowPlayingMovie
    context_object_name = 'movies'
    template_name = 'movies/movie_list.html'
    paginate_by = 10
           
    def get_queryset(self):
        queryset = NowPlayingMovie.objects.all().order_by('-movie_release_date')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Movies List'
        return context