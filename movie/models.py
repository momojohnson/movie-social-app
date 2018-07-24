from django.db import models
from django.utils.text import slugify

# This is the table for the movies that are playing in theater in the USA
class NowPlayingMovie(models.Model):
    movie_title = models.CharField(max_length=1000)
    movie_overview = models.CharField(max_length=1000)
    movie_poster_url = models.CharField(max_length=1000)
    movie_release_date = models.DateField()
    slug = models.SlugField(max_length=500)
    movie_db_id = models.IntegerField()
    movie_trailer_url = models.CharField(max_length=1000)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.movie_title)
        super(NowPlayingMovie, self).save(*args, **kwargs)

    def __str__(self):
        return self.movie_title