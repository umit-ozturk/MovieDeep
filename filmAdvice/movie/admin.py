from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from filmAdvice.movie.models import Movie, WatchHistory, Recommend
from filmAdvice.movie.resources import MovieResource


@admin.register(Movie)
class MovieAdmin(ImportExportModelAdmin):
    list_display = ('movie_name', 'imdb_id', 'movie_pic', 'movie_pic_url', 'slug',)
    search_fields = ('movie_name',)
    resource_class = MovieResource

    readonly_fields = ('slug',)


@admin.register(WatchHistory)
class WatchHistoryAdmin(ImportExportModelAdmin):
    list_display = ('user', 'movie',)
    search_fields = ('movie',)


@admin.register(Recommend)
class RecommendAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'created_at')
    search_fields = ('movie',)