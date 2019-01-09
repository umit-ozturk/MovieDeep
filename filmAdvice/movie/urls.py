from django.urls import path
from filmAdvice.movie.views import MovieView, RecommendView, get_random_movie_request, save_rate_movie

app_name = 'movies'

urlpatterns = [
    path('recommend/<str:slug>/', RecommendView.as_view(template_name="movies/recommend.html"), name='recommend'),
    path('random_movie/', get_random_movie_request, name='get_random_movies'),
    path('save_movie/', save_rate_movie, name='save_rate_movie'),
    path('<str:slug>/', MovieView.as_view(template_name="movies/movie.html"), name='movie_detail'),
]
