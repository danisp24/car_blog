from django.urls import path
from .views import HomeView, AboutView, EditCommentView, DeleteCommentView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('comment/<int:pk>/edit/', EditCommentView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/', DeleteCommentView.as_view(), name='delete_comment')
]
