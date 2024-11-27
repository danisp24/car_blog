from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from FinalProject.posts.models import CarPost


class HomeView(ListView):
    model = CarPost
    template_name = 'common/home.html'
    context_object_name = 'posts'
    paginate_by = 1  # Number of posts per page

    def get_template_names(self):
        if self.request.user.has_perm('posts.can_publish'):
            self.template_name = 'carposts/publisher_car_posts.html'
        elif self.request.user.is_authenticated:
            self.template_name = 'carposts/authenticated_car_posts.html'
        return [self.template_name]

    def get_queryset(self):
        if self.request.user.has_perm('posts.can_publish'):
            return CarPost.objects.all()  # Show all posts for the publisher
        elif self.request.user.is_authenticated:
            return CarPost.objects.filter(is_published=True)  # Show only published posts for authenticated users
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
