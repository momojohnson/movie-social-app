from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from movie.models import NowPlayingMovie
# import movies_data


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

#  model = Campground
#     ontext_object_name = 'campground'
#     pk_url_kwarg = "campground_id"
#     slug_url_kwarg = 'slug'
#     context_object_name = "comments"
#     template_name = 'campgrounds/campground_details.html'
#     paginate_by = 3
    
#     def get_context_data(self, **kwargs):
#         kwargs['campground'] = self.campground
#         kwargs['total_comments'] = Comment.objects.count()
#         return super().get_context_data(**kwargs)
 
    
#     def get_queryset(self):
#         self.campground = get_object_or_404(Campground, pk=self.kwargs.get('campground_id'))
#         queryset = self.campground.comments.order_by("-created_at")
#         return queryset
class MovieDetailsPageView(ListView):
    model = NowPlayingMovie
    pk_url_kwarg = 'movie_id'
    slug_url_kwarg = 'movie_slug'
    template_name = 'movies/movie_details.html'
    # paginate_by = 3
    
    def get_context_data(self, **kwargs):
        kwargs['movie'] = self.movie
        # kwargs['youtube_url'] = movies_data.get_movie_trailer(self.movie.movie_db_id)
        # kwargs['total_comments'] = Comment.objects.count()
        return super().get_context_data(**kwargs)
    
    def get_queryset(self):
        self.movie = get_object_or_404(NowPlayingMovie, pk=self.kwargs.get('movie_id'), slug=self.kwargs.get('movie_slug'))
        # queryset = self.campground.comments.order_by("-created_at")
        
    
    