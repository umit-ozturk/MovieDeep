from django.urls import path
from filmAdvice.movie.views import MovieView, RecommendView, get_random_movies

app_name = 'movies'

urlpatterns = [
    path('<int:movie_id>/', MovieView.as_view(template_name="movies/movie.html"), name='movie_detail'),
    path('recommend/', RecommendView.as_view(template_name="movies/recommend.html"), name='recommend'),
    path('random_movies/', get_random_movies, name='get_random_movies'),
]
