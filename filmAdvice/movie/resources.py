from import_export import resources
from import_export.fields import Field
from filmAdvice.movie.models import Movie
from filmAdvice.system.tools import find_imdb_link_for_movie_id


class MovieResource(resources.ModelResource):
    movie_id = Field(column_name='movieId', attribute='movie_id')
    movie_name = Field(column_name='title', attribute='movie_name')

    class Meta:
        model = Movie
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ['movie_name']

    def before_import_row(self, row, **kwargs):  # Append On Admin Site
        movie_id = row['movieId']
        movie_name = row['title']
        try:
            imdb_id = find_imdb_link_for_movie_id(movie_id)
            if not Movie.objects.filter(movie_name=movie_name).exists():
                Movie.objects.create(movie_id=movie_id, movie_name=movie_name, imdb_id=imdb_id)
        except Exception as ex:
            print(ex)

    def save_instance(self, instance, using_transactions=True, dry_run=False):
        try:
            instance.save()
        except Exception as ex:
            print(ex)
