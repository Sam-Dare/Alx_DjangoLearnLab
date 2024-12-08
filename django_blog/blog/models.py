from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        ordering = ['-published_date']  # Newest posts first

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def profile_picture_url(self):
        """Returns the URL of the profile picture or a default placeholder if not set."""
        if self.profile_picture:
            return self.profile_picture.url
        return '/static/images/default_profile_picture.jpg'  # Replace with your actual default path




class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})
