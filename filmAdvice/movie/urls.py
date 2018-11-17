from django.urls import path
from filmAdvice.movie.views import MovieView

app_name = 'movies'

urlpatterns = [
    path('<int:movie_id>/', MovieView.as_view(template_name="movies/movie.html"), name='movie_detail'),
]
