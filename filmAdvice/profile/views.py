from django.contrib.auth import logout, login, authenticate
from django.urls import reverse
from django.views.generic import FormView, CreateView, RedirectView, DetailView

from filmAdvice.profile.mixins import LoginRequiredMixin
from filmAdvice.profile.forms import RegisterForm, AuthenticationLoginForm
from filmAdvice.profile.models import UserProfile


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
        user = self.get_object()
        return super(ProfileDetailView, self).get_context_data(user=user, **kwargs)
