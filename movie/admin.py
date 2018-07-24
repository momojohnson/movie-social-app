from django.contrib import admin


from . models import NowPlayingMovie

class NowPlayingMovieAdmin(admin.ModelAdmin):
    search_fields = ['movie_title']
admin.site.register(NowPlayingMovie, NowPlayingMovieAdmin)
