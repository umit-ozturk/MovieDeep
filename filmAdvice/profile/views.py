from django.contrib.auth import logout, login, authenticate
from django.urls import reverse
from django.views.generic import FormView, CreateView, RedirectView, DetailView
from django.shortcuts import redirect, render

from filmAdvice.profile.mixins import LoginRequiredMixin
from filmAdvice.profile.forms import RegisterForm, AuthenticationLoginForm
from filmAdvice.profile.models import UserProfile, Relationship
from filmAdvice.movie.models import Movie, Recommend, WatchHistory, WatchList


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "auth/register.html"

    def form_valid(self, form):
        response = super(RegisterView, self).form_valid(form)
        user = authenticate(username=form.cleaned_data["email"],
                            password=form.cleaned_data["password1"])
        login(self.request, user)
        return response

    def get_success_url(self):
        return reverse("home")


class LoginView(FormView):
    form_class = AuthenticationLoginForm
    template_name = "auth/login.html"

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        return reverse("home")

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        return context


class LogoutView(LoginRequiredMixin, RedirectView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

    def get_redirect_url(self, **kwargs):
        return reverse("home")


class ProfileDetailView(DetailView):
    template_name = "auth/profile.html"
    queryset = UserProfile.objects.all()

    def get_context_data(self, **kwargs):
        return super(ProfileDetailView, self).get_context_data(user=self.get_user(), history=self.get_watch_history(),
                                                               watch_list=self.get_watch_list(),
                                                               predictions=self.get_recommendation(), **kwargs)

    def get_user(self):
        return self.get_object()

    def get_recommendation(self):
        return Recommend.objects.filter(user=self.get_user())

    def get_watch_history(self):
        return WatchHistory.objects.filter(user=self.get_user())

    def get_watch_list(self):
        return WatchList.objects.filter(user=self.get_user())

    @staticmethod
    def add_friend(request, username):
        if request.user.is_authenticated():
            user = UserProfile.objects.get_by_natural_key(username)
            Relationship.objects.get_or_create(from_person=request.user, to_person=user)
            return redirect('home')

    @staticmethod
    def show_friends(request, username):
        user = UserProfile.objects.get_by_natural_key(username)
        rel = user.relationships.filter(to_people__from_person=user)
        args = {'friends': rel}
        return render(request, "auth/friend_list.html", args)


class WatchHistoryDetailView(DetailView):
    template_name = "movies/watch_list.html"
    queryset = UserProfile.objects.all()

    def get_context_data(self, **kwargs):
        return super(WatchHistoryDetailView, self).get_context_data(user=self.get_user(),
                                                                    history=self.get_watch_history(), **kwargs)

    def get_user(self):
        return self.get_object()

    def get_watch_history(self):
        return WatchHistory.objects.filter(user=self.get_user())


class WatchListDetailView(DetailView):
    template_name = "movies/watch_list.html"
    queryset = UserProfile.objects.all()

    def get_context_data(self, **kwargs):
        return super(WatchListDetailView, self).get_context_data(user=self.get_user(),
                                                                 watch_list=self.get_watch_list(), **kwargs)

    def get_user(self):
        return self.get_object()

    def get_watch_list(self):
        print(self.get_user())
        print(WatchList.objects.filter(user=self.get_user()))
        return WatchList.objects.filter(user=self.get_user())
