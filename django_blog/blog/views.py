# from django.contrib.auth.views import LoginView, LogoutView
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib import messages
# from django.urls import reverse_lazy
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.contrib.auth.models import User
# from .forms import UserRegistrationForm, UserProfileForm, CommentForm
# from .models import Post, Comment
# from django.db.models import Q
 

# # Custom Authentication Views
# class CustomLoginView(LoginView):
#     template_name = 'blog/login.html'


# class CustomLogoutView(LogoutView):
#     template_name = 'blog/logout.html'


# # User Registration
# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Registration successful. Please log in.')
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'blog/register.html', {'form': form})


# # User Profile Management
# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your profile has been updated.')
#             return redirect('profile')
#     else:
#         form = UserProfileForm(instance=request.user)
#     return render(request, 'blog/profile.html', {'form': form})


# # Blog Post Management
# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/post_list.html'
#     context_object_name = 'posts'
#     ordering = ['-published_date']
#     paginate_by = 5  # Adjust the pagination limit as required


# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'


# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['title', 'content']
#     template_name = 'blog/post_form.html'

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


# class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Post
#     fields = ['title', 'content']
#     template_name = 'blog/post_form.html'

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

#     def test_func(self):
#         post = self.get_object()
#         return self.request.user == post.author


# class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Post
#     template_name = 'blog/post_confirm_delete.html'
#     success_url = reverse_lazy('post-list')

#     def test_func(self):
#         post = self.get_object()
#         return self.request.user == post.author

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     comments = post.comments.all()
#     if request.method == 'POST' and request.user.is_authenticated:
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.author = request.user
#             comment.save()
#             messages.success(request, 'Your comment has been added.')
#             return redirect('post-detail', pk=post.pk)
#     else:
#         form = CommentForm()

#     return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})

# @login_required
# def comment_edit(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     if request.user != comment.author:
#         messages.error(request, "You can only edit your own comments.")
#         return redirect('post-detail', pk=comment.post.pk)

#     if request.method == 'POST':
#         form = CommentForm(request.POST, instance=comment)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your comment has been updated.')
#             return redirect('post-detail', pk=comment.post.pk)
#     else:
#         form = CommentForm(instance=comment)
    
#     return render(request, 'blog/comment_edit.html', {'form': form})

# @login_required
# def comment_delete(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     post_pk = comment.post.pk
#     if request.user != comment.author:
#         messages.error(request, "You can only delete your own comments.")
#     else:
#         comment.delete()
#         messages.success(request, 'Your comment has been deleted.')
#     return redirect('post-detail', pk=post_pk)

# def search_posts(request):
#     query = request.GET.get('q')
#     posts = Post.objects.filter(
#         Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)
#     ).distinct()
#     return render(request, 'blog/search_results.html', {'posts': posts})


# # Search Functionality
# class SearchPostsView(ListView):
#     model = Post
#     template_name = 'blog/search_results.html'
#     context_object_name = 'posts'

#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         return Post.objects.filter(
#             Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)
#         ).distinct()


from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import UserRegistrationForm, UserProfileForm, CommentForm, PostForm
from .models import Post, Comment

# Custom Authentication Views
class CustomLoginView(LoginView):
    template_name = 'blog/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'blog/logout.html'

# # User Registration View
# class UserRegistrationView:
#     def __init__(self, request):
#         self.request = request

#     def register(self):
#         if self.request.method == 'POST':
#             form = UserRegistrationForm(self.request.POST)
#             if form.is_valid():
#                 form.save()
#                 messages.success(self.request, 'Registration successful. Please log in.')
#                 return redirect('login')
#         else:
#             form = UserRegistrationForm()
#         return render(self.request, 'blog/register.html', {'form': form})


# # User Profile Management View
# class UserProfileView(LoginRequiredMixin):
#     def __init__(self, request):
#         self.request = request

#     def profile(self):
#         if self.request.method == 'POST':
#             form = UserProfileForm(self.request.POST, instance=self.request.user)
#             if form.is_valid():
#                 form.save()
#                 messages.success(self.request, 'Your profile has been updated.')
#                 return redirect('profile')
#         else:
#             form = UserProfileForm(instance=self.request.user)
#         return render(self.request, 'blog/profile.html', {'form': form})

# User Registration
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'blog/register.html', {'form': form})


# User Profile Management
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})


# Blog Post Views
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 5  # Adjust the pagination limit as required


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm  # Use your custom form here instead of the default form
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Assign the logged-in user as the author
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# Post Detail View
class CommentCreateView:
    def __init__(self, request, pk):
        self.request = request
        self.pk = pk

    def post_detail(self):
        post = get_object_or_404(Post, pk=self.pk)
        comments = post.comments.all()
        if self.request.method == 'POST' and self.request.user.is_authenticated:
            form = CommentForm(self.request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = self.request.user
                comment.save()
                messages.success(self.request, 'Your comment has been added.')
                return redirect('post-detail', pk=post.pk)
        else:
            form = CommentForm()

        return render(self.request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})


# Comment Edit View
# class CommentEditView(LoginRequiredMixin):
#     def __init__(self, request, pk):
#         self.request = request
#         self.pk = pk

#     def comment_edit(self):
#         comment = get_object_or_404(Comment, pk=self.pk)
#         if self.request.user != comment.author:
#             messages.error(self.request, "You can only edit your own comments.")
#             return redirect('post-detail', pk=comment.post.pk)

#         if self.request.method == 'POST':
#             form = CommentForm(self.request.POST, instance=comment)
#             if form.is_valid():
#                 form.save()
#                 messages.success(self.request, 'Your comment has been updated.')
#                 return redirect('post-detail', pk=comment.post.pk)
#         else:
#             form = CommentForm(instance=comment)
        
#         return render(self.request, 'blog/comment_edit.html', {'form': form})

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        comment = self.get_object()
        if comment.author != self.request.user:
            messages.error(self.request, "You can only edit your own comments.")
            return redirect('post-detail', pk=comment.post.pk)
        form.save()
        messages.success(self.request, 'Your comment has been updated.')
        return redirect('post-detail', pk=comment.post.pk)


# Comment Delete View
class CommentDeleteView(LoginRequiredMixin):
    def __init__(self, request, pk):
        self.request = request
        self.pk = pk

    def comment_delete(self):
        comment = get_object_or_404(Comment, pk=self.pk)
        post_pk = comment.post.pk
        if self.request.user != comment.author:
            messages.error(self.request, "You can only delete your own comments.")
        else:
            comment.delete()
            messages.success(self.request, 'Your comment has been deleted.')
        return redirect('post-detail', pk=post_pk)


# Search View
class SearchPostsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)
        ).distinct()


class TaggedPostsView(ListView):
    model = Post
    template_name = 'blog/tagged_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Get the 'tag_name' from the URL and filter posts by tag
        tag_name = self.kwargs['tag_name']
        return Post.objects.filter(tags__name=tag_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_name = self.kwargs['tag_name']
        context['tag_name'] = tag_name
        return context