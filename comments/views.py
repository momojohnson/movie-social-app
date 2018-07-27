from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views import View

from . models import Comment
from .forms import CommentForm
from movie.models import NowPlayingMovie

@method_decorator(login_required, name='dispatch')
class CreateNewCommentView(View):
    """ create for a comment for a particular movie at route movies/<slug:movie_slug>-<int:movie_id>/comment/add """
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            movie = get_object_or_404(NowPlayingMovie, id= self.kwargs.get('movie_id'), slug=self.kwargs.get('movie_slug') )
            comment.user = request.user
            comment.movie = movie
            comment.save()
            messages.success(request, 'Comment for {} successfully Added.'.format(movie.movie_title))
            return redirect(reverse('movies:movie_details', kwargs={'movie_slug':movie.slug, 'movie_id':movie.pk}))
        
        return render(request, 'comments/new_comment.html', {'form':form, 'movie':movie, 'title':'Add Movie Comment'})
    
    def get(self, request, *args, **kwargs):
        """ Render the form for the user to add a comment """
        """ Render a form for a user to add a comment for a campground at route /campgrounds/<int:campground_id>/<slug:slug>/comments/add """
        movie = get_object_or_404(NowPlayingMovie, id=kwargs.get('movie_id'), slug=kwargs.get('movie_slug'))
        form = CommentForm()
        return render(request, 'comments/new_comment.html', {'form':form, 'movie':movie, 'title':'Add Comment'})
