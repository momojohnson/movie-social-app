from django.db import models

# This is the table for the movies that are playing in theater in the USA
class NowPlayingMovie(models.Model):
    movie_title = models.CharField(max_length=1000)
    movie_overview = models.CharField(max_length=1000)
    movie_poster_url = models.CharField(max_length=1000)
    movie_release_date = models.DateField()
    movie_db_id = models.IntegerField()

if __name__=='__main__':
    movies_now_playing_data()