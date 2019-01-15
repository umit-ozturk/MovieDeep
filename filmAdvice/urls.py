"""filmAdvice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from filmAdvice import settings
from django.conf.urls import include
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from filmAdvice.api.permissions import DocumentAuthenticated
from filmAdvice.movie.views import HomeView
from filmAdvice.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('filmAdvice.api.urls', namespace='api')),
    path('docs/', include_docs_urls(title='Documentation')),
    path('', include('filmAdvice.profile.urls', namespace='profiles')),
    path('', HomeView.as_view(), name='home'),
    path('movie/', include('filmAdvice.movie.urls', namespace='movies')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('oauth-settings/', setting, name='settings'),
    path('oauth-settings/password', password, name='password'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)