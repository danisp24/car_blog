from django.urls import path
from FinalProject.accounts.views import UserLoginView, UserRegisterView, UserLogoutView, EditAccountView, \
    AccountDetailsView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path("details/", AccountDetailsView.as_view(), name="account_details"),
    path("edit-account/", EditAccountView.as_view(), name="edit_account"),
]
