import re
from django import forms
from filmAdvice.profile.models import UserProfile

from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        max_length=30,
        help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'invalid': "Invalid characters"
        }
    )

    class Meta(UserCreationForm.Meta):
        fields = ("full_name", "email", "password", "password2")
        model = UserProfile

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(RegisterForm, self).__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            UserProfile._default_manager.get(username__iexact=username)
        except UserProfile.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
)