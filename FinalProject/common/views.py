from django.contrib import messages
from django.db.models import Case, Value, When, BooleanField
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView

from FinalProject.common.forms import CommentForm
from FinalProject.posts.models import CarPost


class HomeView(ListView):
    model = CarPost
    template_name = 'common/home.html'
    context_object_name = 'posts'
    paginate_by = 3  # Number of posts per page

    def get_template_names(self):
        if self.request.user.has_perm('posts.can_publish'):
            self.template_name = 'carposts/publisher_car_posts.html'
        elif self.request.user.is_authenticated:
            self.template_name = 'carposts/authenticated_car_posts.html'
        return [self.template_name]

    def get_queryset(self):
        if self.request.user.has_perm('posts.can_publish'):
            return (
                CarPost.objects.all(
                )
                .order_by('is_published', '-created_at')
            )
        elif self.request.user.is_authenticated:
            return (
                CarPost.objects.filter(is_published=True)
                .order_by('-created_at')
            )
        else:
            return CarPost.objects.none()

    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('post_id')
        if post_id:
            post = get_object_or_404(CarPost, id=post_id)
            if self.request.user.has_perm('posts.can_publish'):
                post.is_published = not post.is_published  # Toggle the is_published status
                post.save()

        return self.get(request, *args, **kwargs)
