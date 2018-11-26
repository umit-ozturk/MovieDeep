from django.contrib import admin
from filmAdvice.movie.models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_name', 'movie_id', 'imdb_id', 'slug',)
    search_fields = ('movie_name',)

    readonly_fields = ('slug',)


admin.site.register(Movie, MovieAdmin)
