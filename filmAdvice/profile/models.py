from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from filmAdvice.profile.managers import FilmUserManager
from django.db import models
from filmAdvice.profile.constant import *
from django.template.defaultfilters import slugify


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('E-posta', unique=True, null=False, blank=False)
    full_name = models.CharField('İsim', null=True, blank=True, max_length=200)
    phone = models.CharField('Telefon Numarası', null=True, blank=True, max_length=15)
    slug = models.CharField('Slug', null=True, blank=True, max_length=100)
    is_staff = models.BooleanField('Staff Status', default=False)
    status = models.CharField('Üyelik Aşaması', null=True, choices=REGISTER_STATUS, default=EMAIL_CONFIRMATION_NEED,
                              max_length=50)
    is_manager = models.BooleanField('Manager', default=False)
    is_active = models.BooleanField('Active', default=True)
    email_confirmation_token = models.CharField(unique=True, max_length=250, blank=True, null=True)
    email_confirmation_expire_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    password_confirmation_token = models.CharField(unique=True, max_length=250, blank=True, null=True)
    password_confirmation_expire_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    is_email_send = models.BooleanField('Onay E-postası Gönderildi mi?', default=False)
    created_at = models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

    USERNAME_FIELD = 'email'
    objects = FilmUserManager()

    class Meta:
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Kullanıcılar'
        ordering = ('-created_at',)

    def __str__(self):
        return '{}'.format(self.email)

    def get_full_name(self):
        return self.full_name

    def get_slug_field(self):
        return self.email.split("@")[0] + str(self.id)

    def save(self, **kwargs):
        if not self.id:  # if this is a new item
            self.slug = slugify(self.email.split("@")[0])
        super(UserProfile, self).save()
