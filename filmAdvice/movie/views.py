from django.views.generic import TemplateView
from filmAdvice.movie.models import Movie
from filmAdvice.system.tools import *
from filmAdvice.movie.tools import *


class HomeView(TemplateView):
    template_name = "index.html"
    tab_class = "featured"

    paginate_by = 20

    def get_context_data(self, **kwargs):
        return super(HomeView, self).get_context_data(movies=self.get_movies(), **kwargs)

    def get_movies(self):
        return Movie.objects.all()


class MovieView(TemplateView):
    template_name = "movies/movie.html"
    tab_class = "movie_details"

    def get_context_data(self, **kwargs):
        return super(MovieView, self).get_context_data(movie_details=self.get_movie_title,
                                                       movie_ratings=self.get_movie_ratings,
                                                       movie_video=self.get_movie_video, **kwargs)

    def get_movie_title(self, **kwargs):
        imdb_id = find_imdb_link_for_movie_id("2")
        return get_title(imdb_id)

    def get_movie_ratings(self, **kwargs):
        imdb_id = find_imdb_link_for_movie_id("2")
        return get_ratings(imdb_id)

    def get_movie_video(self, **kwargs):
        imdb_id = find_imdb_link_for_movie_id("2")

        youtube = YoutubeAPI()
        print(youtube)
        print(youtube.search(q="Toy Story"))
        return get_video(imdb_id)['videos'][0]['encodings'][0]
