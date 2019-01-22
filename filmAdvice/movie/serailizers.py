from rest_framework import serializers
from filmAdvice.movie.models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ("movie_name", "imdb_id", "slug", "movie_pic_url", )
