from django.core.files.base import ContentFile
import requests
from io import StringIO
from PIL import Image
from django.db import models
from django.utils.text import slugify
from tempfile import NamedTemporaryFile
from filmAdvice.movie.tools import movie_info


class Movie(models.Model):
    movie_id = models.PositiveIntegerField('Film ID', default=0, null=True, blank=True)
    imdb_id = models.CharField('IMDB ID', max_length=25, null=True, blank=True)
    movie_name = models.CharField('Film Adı', max_length=250, null=True, blank=True)
    slug = models.SlugField('Film Slug', null=True, max_length=300, blank=True)
    movie_pic = models.ImageField('Afiş', upload_to='pic_folder/', null=True, blank=True)
    movie_pic_url = models.URLField('Afis URL', null=True, blank=True)
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

    def get_movie_banner(self):
        if not self.movie_pic:
            self.movie_pic_url = movie_info(self.imdb_id)['image']['url']
            self.movie_pic = requests.get(self.movie_pic_url)
        return self.movie_pic

    def save(self, *args, **kwargs):
        if not self.slug:
            if self._get_unique_slug() is not None:
                self.slug = self._get_unique_slug()
            else:
                pass
        super().save(*args, **kwargs)


class WatchHistory(models.Model):
    user = models.ForeignKey('profile.UserProfile', max_length=250, null=True, blank=True, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', max_length=250, null=True, blank=True, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField('Oy', default=0, null=True, blank=True)
    created_at = models.DateTimeField('Kayıt Tarihi', auto_now_add=True, editable=False, null=True, blank=True)
    updated_at = models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False, null=True, blank=True)

    class Meta:
        verbose_name = "İzleme Geçmişim"
        ordering = ('-created_at',)

    def __str__(self):
        return '{}'.format(self.user)


class WatchList(models.Model):
    user = models.ForeignKey('profile.UserProfile', max_length=250, null=True, blank=True, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', max_length=250, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Kayıt Tarihi', auto_now_add=True, editable=False, null=True, blank=True)
    updated_at = models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False, null=True, blank=True)

    class Meta:
        verbose_name = "İzlemek İstediklerim"
        ordering = ('-created_at',)

    def __str__(self):
        return '{}'.format(self.user)


class Recommend(models.Model):
    user = models.ForeignKey('profile.UserProfile', max_length=250, null=True, blank=True, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', max_length=250, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Kayıt Tarihi', auto_now_add=True, editable=False, null=True, blank=True)
    updated_at = models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False, null=True, blank=True)

    class Meta:
        verbose_name = "Tahminler"
        ordering = ('-created_at',)

    def __str__(self):
        return '{}'.format(self.movie)
