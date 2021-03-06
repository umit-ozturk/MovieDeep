import re
from django import forms
from filmAdvice.profile.models import UserProfile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class AuthenticationLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Email address",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'invalid': "Invalid characters"
        }
    )
    password = forms.CharField(
        label="Create password",
        max_length=30,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'invalid': "Invalid characters"
        }
    )

    class Meta(AuthenticationForm):
        fields = ("username", "password",)
        model = UserProfile

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        kwargs.setdefault('label_suffix', '')
        super(AuthenticationForm, self).__init__(*args, **kwargs)


class RegisterForm(UserCreationForm):
    full_name = forms.CharField(
        label="Full name",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'invalid': "Invalid characters"
        }
    )
    email = forms.CharField(
        label="Email address",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'invalid': "Invalid characters"
        }
    )
    password1 = forms.CharField(
        label="Create password",
        max_length=30,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'invalid': "Invalid characters"
        }
    )
    password2 = forms.CharField(
        label="Repeat password",
        max_length=30,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'invalid': "Invalid characters"
        }
    )

    class Meta(UserCreationForm.Meta):
        fields = ("email", "password1", "password2")
        exclude = ['username', ]
        model = UserProfile

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(RegisterForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            UserProfile.objects.get(email__iexact=email)
        except UserProfile.DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages['duplicate_email'],
            code='duplicate_username',
        )
