import re
from django import forms
from filmAdvice.profile.models import UserProfile

from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    username = forms.RegexField(
        label=_("Username"),
        max_length=30, regex=re.compile(r'^[\w\s-]+$', re.LOCALE),
        help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'invalid': _("Invalid characters")
        }
    )

    class Meta(UserCreationForm.Meta):
        fields = ("username", "email")
        model = UserProfile

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(RegistrationForm, self).__init__(*args, **kwargs)

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            UserProfile._default_manager.get(username__iexact=username)
        except UserProfile.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
)