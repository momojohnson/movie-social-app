import os

from decouple import config
import requests
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movieproject.settings')
import django
django.setup()
from movie.models import NowPlayingMovie

API_KEY = config('API_KEY')

# Get the total number of pages of movies that are playing in USA from the themoviedb.org
def number_of_pages_of_movies_now_playing():
    url = "https://api.themoviedb.org/3/movie/now_playing?api_key={}&language=en-US&page=1&region=US".format(API_KEY)
    json_data = requests.get(url).json()
    pages = json_data['total_pages']
    return pages

# Get the urls per page for movies that are now playing in theaters within the USA
# and add them to the movies playing url list
def list_of_movies_now_playing_urls():
    movies_playing_urls_list = list()
    for page_number in range(1, number_of_pages_of_movies_now_playing()+1):
        print("Page Number" + str(page_number))# For debugging purposes
        url = "https://api.themoviedb.org/3/movie/now_playing?api_key={}&language=en-US&page={}&region=US".format(API_KEY, page_number)
        movies_playing_urls_list.append(url)
    return movies_playing_urls_list

# Retrieving data for movies that are now playing in theater in the USA
def movies_now_playing_data():
    movies_url = list_of_movies_now_playing_urls()
    for urls in movies_url:
        movies_playing_json = requests.get(urls).json()
        # Get the total number of results on each page  and retrieve the specified fields
        for i in range(len(movies_playing_json['results'])):
            movie_title = movies_playing_json['results'][i]['title']
            movie_db_id  = movies_playing_json['results'][i]['id']
            movie_overview = movies_playing_json['results'][i]['overview']
            movie_poster_url = movies_playing_json['results'][i]['poster_path']
            if movie_poster_url:
                movie_poster_url = "https://image.tmdb.org/t/p/w500"+ str(movies_playing_json['results'][i]['poster_path'])
            else:
                movie_poster_url = "https://www.freeiconspng.com/uploads/no-image-icon-11.PNG"
            movie_release_date = movies_playing_json['results'][i]['release_date']
            NowPlayingMovie.objects.get_or_create(movie_title=movie_title, movie_overview=movie_overview, movie_poster_url=movie_poster_url,movie_release_date=movie_release_date, movie_db_id=movie_db_id)

if __name__=='__main__':
    movies_now_playing_data()