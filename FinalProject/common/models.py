from django.contrib.auth import get_user_model
from django.db import models

from FinalProject.posts.models import CarPost

UserModel = get_user_model()


class Comment(models.Model):
    post = models.ForeignKey(
        CarPost,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
