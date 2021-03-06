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
        url = "https://api.themoviedb.org/3/movie/now_playing?api_key={}&language=en-US&video=true&page={}&region=US".format(API_KEY, page_number)
        movies_playing_urls_list.append(url)
    return movies_playing_urls_list
    
# Return a movie trailer if the movie has a trailer, otherwise return None   
def get_movie_trailer(movie_id):
    trailer_url = 'http://api.themoviedb.org/3/movie/{}/videos?api_key={}'.format(movie_id, API_KEY)
    json_response = requests.get(trailer_url).json()
    trailer_video_url = None
    if json_response.get('results'):
        youtube_trailer_key = json_response.get('results')[0].get('key')
        trailer_video_url = 'https://www.youtube.com/embed/{}'.format(youtube_trailer_key)
        print(trailer_video_url)

    return trailer_video_url

# Retrieving movies data that are now playing in theater in USA and also contain poster and trailer url
def movies_now_playing_data():
    movies_url = list_of_movies_now_playing_urls()
    for urls in movies_url:
        print(urls)
        movies_playing_json = requests.get(urls).json()
        # Get the total number of results on each page  and retrieve the specified fields
        if movies_playing_json.get('results'):
            for i in range(len(movies_playing_json['results'])):
                movie_poster_url = movies_playing_json['results'][i].get('poster_path')
                movie_trailer_url = get_movie_trailer(movies_playing_json['results'][i].get('id'))
                # Check if the movie has movie_poster_url and movie_trailer_url
                if movie_poster_url and movie_trailer_url:
                    movie_title = movies_playing_json['results'][i].get('title')
                    movie_db_id  = movies_playing_json['results'][i].get('id')
                    movie_overview = movies_playing_json['results'][i].get('overview')
                    movie_poster_url = "https://image.tmdb.org/t/p/w500"+ str(movies_playing_json['results'][i]['poster_path'])
                    movie_release_date = movies_playing_json['results'][i]['release_date']
                    NowPlayingMovie.objects.get_or_create(movie_title=movie_title, movie_overview=movie_overview, movie_poster_url=movie_poster_url,
                    movie_release_date=movie_release_date, movie_db_id=movie_db_id,
                    movie_trailer_url=movie_trailer_url)
                else:
                    pass
        else:
            pass
            


   
    
if __name__=='__main__':
    movies_now_playing_data()
    