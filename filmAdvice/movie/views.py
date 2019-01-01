from django.views.generic import TemplateView
from filmAdvice.movie.models import Movie
from filmAdvice.system.tools import *
from filmAdvice.movie.tools import *


class HomeView(TemplateView):
    template_name = "index.html"
    tab_class = "featured"

    paginate_by = 20

    def get_context_data(self, **kwargs):
        imdb_id = "tt0114709"
        return super(HomeView, self).get_context_data(movies=self.get_popular_movies(),
                                                      movie_data=self.get_movie_info(imdb_id), **kwargs)

    def get_popular_movies(self):
        return popular_movies()

    def get_movies(self):
        return Movie.objects.all()

    def get_movie_info(self, imdb_id):
        return movie_info(imdb_id)


class MovieView(TemplateView):
    template_name = "movies/movie.html"

    def get_context_data(self, **kwargs):
        imdb_id = "tt0114709"  # imdb_id = find_imdb_link_for_movie_id("1") --> Temporary static variable
        movie_base_data = self.get_movie_info(imdb_id)
        return super(MovieView, self).get_context_data(movie_data=movie_base_data,
                                                       movie_ratings=self.get_movie_ratings(imdb_id),
                                                       movie_crew=self.get_title_crew(imdb_id),
                                                       movie_video=self.get_movie_video(movie_base_data['title'],
                                                                                        movie_base_data['year']),
                                                       movie_genres=self.get_movie_genres(imdb_id), **kwargs)

    def get_movie_info(self, imdb_id):
        movie_data = (imdb_id)
        return movie_data

    def get_title_crew(self, imdb_id):
        return crew_info(imdb_id)

    def get_movie_ratings(self, imdb_id):
        return movie_ratings(imdb_id)

    def get_movie_video(self, movie_title, movie_year):
        return youtube_search(q=str(movie_title), year=str(movie_year))['videoId'][0]

    def get_movie_genres(self, imdb_id):
        return movie_genres(imdb_id)['genres']
