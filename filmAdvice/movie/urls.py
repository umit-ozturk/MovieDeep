from django.urls import path
from filmAdvice.movie.views import MovieView, RecommendView, get_random_movies

app_name = 'movies'

urlpatterns = [
    path('recommend/', RecommendView.as_view(template_name="movies/recommend.html"), name='recommend'),
    path('random_movie/', get_random_movies, name='get_random_movies'),
]
