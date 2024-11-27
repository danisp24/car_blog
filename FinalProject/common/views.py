from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from FinalProject.posts.models import CarPost


class HomeView(TemplateView):
    template_name = 'common/home.html'

    def get_template_names(self):
        if self.request.user.has_perm('posts.can_publish'):
            self.template_name = 'carposts/publisher_car_posts.html'
        elif self.request.user.is_authenticated:
            self.template_name = 'carposts/authenticated_car_posts.html'
        return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.has_perm('posts.can_publish'):
            context['posts'] = CarPost.objects.all()
        elif self.request.user.is_authenticated:
            context['posts'] = CarPost.objects.filter(is_published=True)
        else:
            context['posts'] = []

        return context

    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('post_id')
        if post_id:
            post = get_object_or_404(CarPost, id=post_id)
            if self.request.user.has_perm('posts.can_publish'):
                post.is_published = not post.is_published  # Toggle the is_published status
                post.save()

        return self.get(request, *args, **kwargs)
