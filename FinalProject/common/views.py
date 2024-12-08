from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, TemplateView, UpdateView, DeleteView

from FinalProject.cars.models import CarCategory
from FinalProject.common.forms import CommentForm
from FinalProject.common.models import Comment
from FinalProject.posts.forms import SearchForm
from FinalProject.posts.models import CarPost


class HomeView(ListView, FormView):
    model = CarPost
    template_name = 'common/home.html'
    context_object_name = 'posts'
    paginate_by = 3
    form_class = SearchForm

    def get_template_names(self):
        if self.request.user.is_authenticated:
            self.template_name = 'carposts/authenticated_car_posts.html'
        return self.template_name

    def get_queryset(self):

        if self.request.user.has_perm('posts.can_publish'):
            queryset = CarPost.objects.all()

        elif self.request.user.is_authenticated:
            queryset = CarPost.objects.filter(is_published=True)

        else:
            queryset = CarPost.objects.none()

        if 'query' in self.request.GET:
            query = self.request.GET.get('query')
            if query:
                queryset = queryset.filter(
                    Q(title__icontains=query) | Q(content__icontains=query)
                )

        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(related_cars__category_id=category_id).distinct()
        queryset = queryset.order_by('is_published', '-created_at')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CarCategory.objects.all()
        context['selected_category'] = self.request.GET.get('category', '')
        return context

    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('post_id')
        if post_id:
            post = get_object_or_404(CarPost, id=post_id)
            if self.request.user.has_perm('posts.can_publish'):
                post.is_published = not post.is_published
                post.save()

        return self.get(request, *args, **kwargs)


class AboutView(TemplateView):
    template_name = "common/about.html"


class EditCommentView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = 'common/edit_comment.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.object.post
        return context

    def get_success_url(self):
        return reverse_lazy('detail_post', kwargs={'pk': self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user


class DeleteCommentView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse_lazy('detail_post', kwargs={'pk': self.object.post.id})

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user
