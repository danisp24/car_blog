from django.urls import path

from FinalProject.posts.views import CarPostCreateView, MyPostsView, EditPostView, DeletePostView, DetailPostView

urlpatterns = [
    path('create/', CarPostCreateView.as_view(), name='create_car_post'),
    path('my-posts/', MyPostsView.as_view(), name='my_posts'),
    path('edit-post/<int:pk>/', EditPostView.as_view(), name='edit_post'),
    path('delete-post/<int:pk>/', DeletePostView.as_view(), name='delete_post'),
    path('detail-post/<int:pk>/', DetailPostView.as_view(), name='detail_post'),
]
