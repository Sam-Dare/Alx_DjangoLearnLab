from django.urls import path
from .views import RegisterView, login_view, follow_user, unfollow_user, UserProfileView

urlpatterns = [
    # User registration route
    path('register/', RegisterView.as_view(), name='register'),
    
    # User login route
    path('login/', login_view, name='login'),
    
    # User follow/unfollow routes
    path('follow/<int:user_id>/', follow_user, name='follow'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow'),
    
    # User profile route (view and update profile)
    path('profile/', UserProfileView.as_view(), name='profile'),
]
