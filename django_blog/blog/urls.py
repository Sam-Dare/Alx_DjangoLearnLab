from django.urls import path
from .views import (
    CustomLoginView,
    CustomLogoutView,
    register,
    profile,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostDetailViewWithComments,
    CommentEditView,
    CommentDeleteView,
    SearchPostsView,
    TaggedPostsView
)

urlpatterns = [
    # Authentication URLs
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),

    # Blog Post URLs
    path('', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Tagged Post URLs
    path('tags/<str:tag_name>/', TaggedPostsView, name='tagged-posts'),

    # Comment URLs
    path('post/<int:pk>/', PostDetailViewWithComments, name='post-detail'),
    path('comments/<int:pk>/edit/', CommentEditView, name='comment-edit'),
    path('comments/<int:pk>/delete/', CommentDeleteView, name='comment-delete'),

    # Search URLs
    path('search/', SearchPostsView, name='search'),
]
