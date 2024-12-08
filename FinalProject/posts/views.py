from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, FormView
from django.views.generic.edit import FormMixin
from FinalProject.common.forms import CommentForm
from FinalProject.posts.forms import PostCreateForm, PostDeleteForm, PostEditForm
from FinalProject.posts.models import CarPost


class CarPostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = CarPost
    form_class = PostCreateForm
    template_name = 'carposts/create_car_post.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.is_published = False
        return super().form_valid(form)

    def handle_no_permission(self):
        return redirect(self.login_url)


class MyPostsView(LoginRequiredMixin, ListView):
    model = CarPost
    template_name = 'carposts/my_posts.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return CarPost.objects.filter(author=self.request.user).order_by('-created_at')


class EditPostView(LoginRequiredMixin, UpdateView):
    model = CarPost
    form_class = PostEditForm
    template_name = 'carposts/edit_post.html'

    def get_queryset(self):
        return CarPost.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('my_posts')


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


class DetailPostView(LoginRequiredMixin, FormMixin, DetailView):
    model = CarPost
    template_name = 'carposts/post_detail.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_object(self):
        post_id = self.kwargs.get('pk')
        post = get_object_or_404(CarPost, pk=post_id)

        if not post.is_published and not self.request.user.has_perm('posts.can_publish'):
            raise PermissionDenied

        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()

        comments_list = post.comments.all().order_by('-created_at')
        paginator = Paginator(comments_list, 3)

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['comments'] = page_obj
        if self.request.user.is_authenticated and post.is_published:
            context['comment_form'] = self.get_form()

        context['page_obj'] = page_obj

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = self.request.user
            comment.save()
            return redirect('detail_post', pk=self.object.pk)

        context = self.get_context_data(form=form)
        return self.render_to_response(context)
