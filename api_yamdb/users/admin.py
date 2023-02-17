# abstract_user/users/admin.py
from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'bio',
        'role',
        'confirmation_code',
    )
    search_fields = ('username', 'role')


admin.site.register(User, UserAdmin)
