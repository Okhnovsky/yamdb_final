from django.contrib.auth.models import AbstractUser
from django.db import models
from .enumerates import ROLE_CHOICES
from .validators import validate_username


class User(AbstractUser):
    """Кастомная модель пользователя."""

    username = models.CharField(
        'Имя пользователя',
        validators=(validate_username,),
        max_length=150,
        unique=True,
        blank=False,
        null=False
    )
    email = models.EmailField(
        'Email пользователя',
        max_length=254,
        unique=True,
        blank=False,
        null=False
    )
    first_name = models.CharField(
        'Имя',
        max_length=150,
        blank=True
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        blank=True
    )
    bio = models.TextField(
        'Биография',
        blank=True
    )
    role = models.CharField(
        'Роль',
        max_length=20,
        choices=ROLE_CHOICES,
        default='user',
        blank=True
    )
    confirmation_code = models.CharField(
        'Код подтверждения',
        max_length=255,
        null=True,
        blank=False
    )

    @property
    def is_user(self):
        return self.role == 'user'

    @property
    def is_admin(self):
        return self.role == ('admin' or self.is_superuser
                             or self.is_staff)

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    def __str__(self):
        return self.username
