from django.db import models


class Movie(models.Model):
    movie_id = models.PositiveIntegerField('Film ID', default=0)
    imdb_id = models.PositiveIntegerField('IMDB ID', default=0)
    movie_name = models.CharField('Film Adı', max_length=150, default="")
    slug = models.SlugField(null=True)
    created_at = models.DateTimeField('Kayıt Tarihi', auto_now_add=True, editable=False, null=True, blank=True)
    updated_at = models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False, null=True, blank=True)

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Filmler"
        ordering = ('-created_at',)

    def __str__(self):
        return '{}'.format(self.movie_name)
