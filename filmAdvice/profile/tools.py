import django.contrib.auth.password_validation as validators
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from filmAdvice.profile.models import UserProfile


def create_user_profile(user, params):
    try:
        if user and user.is_authenticated:
            raise Exception("Zaten giriş yapmış durumdasınız.")
        if UserProfile.objects.filter(email=params["user"]["email"]).exists():
            raise Exception('Lütfen başka bir e-posta adresi kullanın.')
        password = params["user"]['password']
        password_again = params["user"]['password_again']
        if password != password_again:
            raise Exception('Girdiğiniz parolalar aynı değil. Lütfen tekrar deneyiniz..')
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
        raise ex("Kullanıcı Profili Oluşturulamadı.")
