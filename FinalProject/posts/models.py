from django.db import models


class CarPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # related_cars = models.ManyToManyField('Car', blank=True)  # TODO
    is_published = models.BooleanField(default=False)  # Visibility control

    class Meta:
        permissions = [
            ("can_publish", "Can publish car posts"),
        ]

    def __str__(self):
        return self.title
