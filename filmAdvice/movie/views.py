from django.views.generic import TemplateView, ListView, DetailView
from filmAdvice.movie.models import Movie
from filmAdvice.system.load_data import LoadDataSets
from filmAdvice.system.tools import find_imdb_ib_for_movie_id


class HomeView(TemplateView):
    template_name = "index.html"
    tab_class = "featured"

    paginate_by = 20

    def get_context_data(self, **kwargs):
        return super(HomeView, self).get_context_data(movies=self.get_movies(), **kwargs)

    def get_movies(self):
        return Movie.objects.all()


class MovieListView(ListView):
    template_name = "movies/movie.html"
    queryset = Movie.objects.all()

    def get_context_data(self, **kwargs):
        a = find_imdb_ib_for_movie_id("1")
        print(a)
        return super(MovieListView, self).get_context_data(id=None, **kwargs)

    def get_movie_id(self, **kwargs):
        return LoadDataSets.load_movie_data()