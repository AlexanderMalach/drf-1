from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """
    Модель пользователя.
    """

    username = None
    email = models.EmailField(
        unique=True, verbose_name="Email адрес", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=35,
        **NULLABLE,
        verbose_name="Номер телефона",
        help_text="Укажите номер телефона"
    )
    city = models.CharField(
        max_length=50, **NULLABLE, verbose_name="Город", help_text="Укажите ник город"
    )
    avatar = models.ImageField(
        upload_to="users/avatar",
        **NULLABLE,
        verbose_name="Аватар",
        help_text="Загрузите аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
