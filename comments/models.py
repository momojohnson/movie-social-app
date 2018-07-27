from django.db import models
from django.contrib.auth.models import User
from movie.models import NowPlayingMovie

class Comment(models.Model):
    """Comment model for campground """
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    now_playing_movie = models.ForeignKey(NowPlayingMovie, related_name='moives_playing', on_delete=models.CASCADE)
