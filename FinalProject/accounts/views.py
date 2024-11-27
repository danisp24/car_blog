from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from FinalProject.accounts.forms import CustomAuthenticationForm, CustomUserCreationForm


# Create your views here.

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
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
