from django.urls import path
from filmAdvice.api.views import *

app_name = 'api'

urlpatterns = [
    path('hello/', hello),
]