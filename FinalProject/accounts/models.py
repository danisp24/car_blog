from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from FinalProject.accounts.validators import OnlyLettersValidator


class AppUser(AbstractUser):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    MAX_FIRST_NAME_LENGTH = 20
    MAX_LAST_NAME_LENGTH = 20
    MIN_NAME_LENGTH = 2

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        null=True,
        blank=True,
        validators=[
            MinLengthValidator(MIN_NAME_LENGTH),
            OnlyLettersValidator(),
        ],
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        null=True,
        blank=True,
        validators=[
            MinLengthValidator(MIN_NAME_LENGTH),
            OnlyLettersValidator(),
        ],
    )

    gender = models.CharField(
        max_length=8,
        choices=GENDER_CHOICES,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"User: {self.username}"
