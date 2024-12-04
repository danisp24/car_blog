from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import get_messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, FormView
from FinalProject.posts.forms import PostCreateForm, PostDeleteForm, SearchForm
from FinalProject.posts.models import CarPost


class CarPostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = CarPost
    form_class = PostCreateForm
    template_name = 'carposts/create_car_post.html'
    success_url = reverse_lazy('home')
    success_message = "Your post has been created successfully!"
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.is_published = False
        return super().form_valid(form)

    def handle_no_permission(self):
        messages.error(self.request, "You need to be logged in to make a post. Please sign in.")
        return redirect(self.login_url)


class MyPostsView(LoginRequiredMixin, ListView):
    model = CarPost
    template_name = 'carposts/my_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return CarPost.objects.filter(author=self.request.user)


class EditPostView(LoginRequiredMixin, UpdateView):
    model = CarPost
    fields = ['title', 'content', ]
    template_name = 'carposts/edit_post.html'

    def get_queryset(self):
        return CarPost.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('my_posts')

    # class DeletePostView(LoginRequiredMixin, DeleteView):
    #     model = CarPost
    #     template_name = 'carposts/delete_post.html'
    #     success_url = reverse_lazy('my_posts')
    #
    #     def get_queryset(self):
    #         return CarPost.objects.filter(author=self.request.user)


class DeletePostView(LoginRequiredMixin, DeleteView, FormView):
    model = CarPost
    template_name = 'carposts/delete_post.html'
    context_object_name = 'post'
    success_url = reverse_lazy('home')
    form_class = PostDeleteForm

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = CarPost.objects.get(pk=pk)
        return post.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class DetailPostView(LoginRequiredMixin, DetailView):
    model = CarPost
    template_name = 'carposts/post_detail.html'
    context_object_name = 'post'

    def get_object(self):
        post_id = self.kwargs.get('pk')
        return get_object_or_404(CarPost, pk=post_id)
