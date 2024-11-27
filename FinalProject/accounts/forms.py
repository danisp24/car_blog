from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        "invalid_login": _(
            "The username and password combination is incorrect. Please try again."
        ),
        "inactive": _("This account is inactive."),
    }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "gender",
            "password1",
            "password2",
        ]
        widgets = {
            "gender": forms.Select(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }
