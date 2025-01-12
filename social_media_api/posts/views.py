from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from notifications.models import Notification
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics  # Correctly importing generics

# Custom permission to ensure only the author can edit or delete their post/comment
class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Only allow editing/deleting if the user is the author
        return obj.author == request.user

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if created:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target=post
        )
        return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
    return Response({"message": "Post already liked"}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    # Using generics.get_object_or_404 to fetch the post
    post = generics.get_object_or_404(Post, pk=pk)
    like = Like.objects.filter(user=request.user, post=post).first()

    if like:
        like.delete()
        return Response({"message": "Post unliked"}, status=status.HTTP_200_OK)
    return Response({"message": "You have not liked this post"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_feed(request):
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthor()]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # Use generics.get_object_or_404 here to retrieve the Post object by pk
    def get_object(self):
        # Using generics.get_object_or_404 to get the post object
        obj = generics.get_object_or_404(Post, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the author of the comment to the currently authenticated user
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthor()]
        return super().get_permissions()