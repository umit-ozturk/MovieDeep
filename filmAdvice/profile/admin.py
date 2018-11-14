from django.contrib import admin
from filmAdvice.profile.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'status', 'is_email_send',)
    search_fields = ('email',)

    readonly_fields = ('is_email_send', 'password_confirmation_token', 'password_confirmation_expire_date', 'last_login',)


admin.site.register(UserProfile, UserProfileAdmin)
