from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from filmAdvice.movie.models import Movie
from filmAdvice.movie.resources import MovieResource


@admin.register(Movie)
class MovieAdmin(ImportExportModelAdmin):
    list_display = ('movie_name', 'movie_id', 'imdb_id', 'slug',)
    search_fields = ('movie_name',)
    resource_class = MovieResource

    readonly_fields = ('slug',)
