from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from filmAdvice.profile.constant import *


class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Kullanıcı Adı', unique=True, null=False, blank=False, max_length=100)
    email = models.EmailField('E-posta', unique=True, null=False, blank=False)
    name = models.CharField('İsim', null=True, blank=True, max_length=100)
    surname = models.CharField('Soyisim', null=True, blank=True, max_length=100)
    phone = models.CharField('Telefon Numarası', null=True, blank=True, max_length=15)
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

    class Meta:
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Kullanıcılar'
        ordering = ('-created_at',)

    def __str__(self):
        return '{}'.format(self.email)

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def get_account_name(self):
        return '{}-{}'.format(self.name.lower(), self.surname.lower())