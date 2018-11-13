import django.contrib.auth.password_validation as validators
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from filmAdvice.profile.models import UserProfile


def create_user_profile(user, params):
    try:
        if user and user.is_authenticated:
            raise Exception("You're already logged in.")
        if UserProfile.objects.filter(email=params["user"]["email"]).exists():
            raise Exception('Please use another email address.')
        password = params["user"]['password']
        password_again = params["user"]['password_again']
        if password != password_again:
            raise Exception('The passwords you entered are not the same. Please try again.')
        else:
            try:
                validators.validate_password(password)
            except ValidationError as exc:
                raise Exception('; '.join(exc.messages))
            params["user"]["password"] = make_password(password)
            params["user"].pop("password_again")
            profile = UserProfile(**params["user"])
            profile.save()
            return profile
    except Exception as ex:
        raise ex("Couldn't Create User Profile.")
