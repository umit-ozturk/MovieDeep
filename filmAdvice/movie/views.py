from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, DetailView
from django.shortcuts import HttpResponse
from filmAdvice.movie.serailizers import MovieSerializer
from filmAdvice.movie.models import Movie
from filmAdvice.movie.tools import *
import random
import json


@login_required
def get_random_movies(request):
    if request.is_ajax():
        random_movie = random.sample(list(Movie.objects.all()), k=1)
        serialized_random_movie = MovieSerializer(random_movie, many=True).data
        return HttpResponse(json.dumps({'message': "Its Ok", 'random_movie': serialized_random_movie}),
                            content_type='application/json')
    return HttpResponse(json.dumps({'message': "Something Went Wrong, Sorry :("}))


@login_required
@csrf_exempt
def save_rate_movie(request):
    if request.is_ajax():
        rate = request.POST.get('rate')
        if isinstance(int(rate), int) and int(rate) in range(0, 6):
            return HttpResponse(json.dumps({'message': "Its Ok"}), content_type='application/json')
    return HttpResponse(json.dumps({'message': "Something Went Wrong, Sorry :("}))


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(movies=self.get_popular_movies(), **kwargs)
        return context

    def get_popular_movies(self):
        return popular_movies()['ranks'][:24]


class MovieView(DetailView):
    template_name = "movies/movie.html"
    model = Movie

    def get_context_data(self, **kwargs):
        imdb_id = Movie.objects.filter(slug=self.kwargs['slug'])[0].imdb_id
        movie_base_data = self.get_movie_info(imdb_id)
        return super(MovieView, self).get_context_data(movie_data=movie_base_data,
                                                       movie_ratings=self.get_movie_ratings(imdb_id),
                                                       movie_crew=self.get_title_crew(imdb_id),
                                                       movie_video=self.get_movie_video(movie_base_data['title'],
                                                                                        movie_base_data['year']),
                                                       movie_genres=self.get_movie_genres(imdb_id), **kwargs)

    def get_movie_info(self, imdb_id):
        movie_data = movie_info(imdb_id)
        return movie_data

    def get_title_crew(self, imdb_id):
        return crew_info(imdb_id)

    def get_movie_ratings(self, imdb_id):
        return movie_ratings(imdb_id)

    def get_movie_video(self, movie_title, movie_year):
        return youtube_search(q=str(movie_title), year=str(movie_year))['videoId'][0]

    def get_movie_genres(self, imdb_id):
        return movie_genres(imdb_id)['genres']


class RecommendView(TemplateView):
    template_name = "movies/recommend.html"

    def get_context_data(self, **kwargs):
        return super(RecommendView, self).get_context_data()
