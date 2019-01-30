import requests
from django.db import models
from django.utils.text import slugify
from filmAdvice.movie.tools import movie_info
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


class Movie(models.Model):
    movie_id = models.PositiveIntegerField('Film ID', default=0, null=True, blank=True)
    imdb_id = models.CharField('IMDB ID', max_length=25, null=True, blank=True)
    movie_name = models.CharField('Film Adı', max_length=250, null=True, blank=True)
    slug = models.SlugField('Film Slug', null=True, max_length=300, blank=True)
    movie_pic = models.ImageField('Afiş', upload_to='pic_folder/', null=True, blank=True)
    movie_pic_url = models.CharField('Afis URL', max_length=200, null=True, blank=True)
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
        print("Debug0")
        if not self.movie_pic:
            movie = Movie.objects.filter(movie_id=self.movie_id)[0]
            movie_pic_url = movie_info(movie.imdb_id)['image']['url']
            image = requests.get(movie_pic_url).content
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(image)
            img_temp.flush()
            movie.movie_pic.save(self.movie_name + ".jpg", File(img_temp), save=True)
            movie.movie_pic_url = self.movie_name + ".jpg"
            movie.save()
        return self.movie_pic_url

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
