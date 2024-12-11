from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from FinalProject.accounts.forms import CustomAuthenticationForm, CustomUserCreationForm, CustomUserEditForm

AppUser = get_user_model()


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')
    authentication_form = CustomAuthenticationForm

    def get_success_url(self):
        return self.success_url

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


class UserLogoutView(LogoutView):
    pass


class UserRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseForbidden(render(request, '403.html'))
        return super().dispatch(request, *args, **kwargs)


class AccountDetailsView(LoginRequiredMixin, DetailView):
    model = AppUser
    template_name = "registration/account_details.html"
    context_object_name = "user_details"

    def get_object(self, queryset=None):
        return self.request.user


class EditAccountView(LoginRequiredMixin, UpdateView):
    model = AppUser
    form_class = CustomUserEditForm
    template_name = "registration/edit_account.html"
    success_url = reverse_lazy("account_details")

    def get_object(self, queryset=None):
        return self.request.user
