from rest_framework import serializers
from filmAdvice.movie.models import Movie
from filmAdvice.movie.tools import movie_info


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ("movie_name", "imdb_id", "slug", "get_movie_banner", )
