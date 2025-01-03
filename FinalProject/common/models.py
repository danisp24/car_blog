from django.contrib.auth import get_user_model
from django.db import models

from FinalProject.posts.models import CarPost

AppUser = get_user_model()


class Comment(models.Model):
    post = models.ForeignKey(
        CarPost,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE
    )

    content = models.TextField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)
