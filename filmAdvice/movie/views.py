from django.views.generic import TemplateView
from filmAdvice.movie.models import Movie


class HomeView(TemplateView):
    template_name = "index.html"
    tab_class = "featured"

    paginate_by = 20

    def get_context_data(self, **kwargs):
        return super(HomeView, self).get_context_data(moview=self.get_movies(), **kwargs)

    def get_movies(self):
        return Movie.objects.all()
