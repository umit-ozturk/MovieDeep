from django.urls import path
from filmAdvice.profile.views import LoginView, LogoutView, RegisterView, ProfileDetailView, WatchListDetailView, \
    WatchHistoryDetailView

app_name = 'profiles'

urlpatterns = [
    path('login/', LoginView.as_view(template_name="auth/login.html"), name='auth_login'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('register/', RegisterView.as_view(template_name="auth/register.html"), name='auth_registration'),
    path('user/<str:slug>/', ProfileDetailView.as_view(template_name="auth/profile.html"), name='auth_profile'),
    path('history/<str:slug>/', WatchHistoryDetailView.as_view(template_name="movies/watch_history.html"), name='watch_history'),
    path('list/<str:slug>/', WatchListDetailView.as_view(template_name="movies/watch_list.html"), name='watch_list'),
    path('friends/<str:slug>/', ProfileDetailView.show_friends, name='friends_list'),
]
