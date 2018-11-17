from django.urls import path
from filmAdvice.movie.views import MovieListView

app_name = 'movies'

urlpatterns = [
    path('', MovieListView.as_view(template_name="movies/movie.html"), name='movies'),
]
