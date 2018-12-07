from django.db import models
from django.utils.text import slugify


class Movie(models.Model):
    movie_id = models.PositiveIntegerField('Film ID', default=0, null=True, blank=True)
    imdb_id = models.CharField('IMDB ID', max_length=25, null=True, blank=True)
    movie_name = models.CharField('Film Adı', max_length=250, null=True, blank=True)
    slug = models.SlugField('Film Slug', null=True, max_length=300, blank=True)
    created_at = models.DateTimeField('Kayıt Tarihi', auto_now_add=True, editable=False, null=True, blank=True)
    updated_at = models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False, null=True, blank=True)

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Filmler"
        ordering = ('-created_at',)

    def __str__(self):
        return '{}'.format(self.movie_name)

    def _get_unique_slug(self):
        try:
            slug = slugify(self.movie_name)
            unique_slug = '{}'.format(slug)
            return unique_slug
        except Exception as ex:
            print(ex)
            pass

    def save(self, *args, **kwargs):
        if not self.slug:
            if self._get_unique_slug() is not None:
                print(self._get_unique_slug())
                self.slug = self._get_unique_slug()
            else:
                pass
        super().save(*args, **kwargs)
