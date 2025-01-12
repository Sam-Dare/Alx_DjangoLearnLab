from django.urls import path
from .views import RegisterView, LoginView, FollowUserView, UnfollowUserView, UserProfileView

urlpatterns = [
    # User registration route
    path('register/', RegisterView.as_view(), name='register'),
    
    # User login route
    path('login/', LoginView.as_view(), name='login'),  # Corrected to use LoginView
    
    # User follow/unfollow routes
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow'),  # Corrected to use FollowUserView
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow'),  # Corrected to use UnfollowUserView
    
    # User profile route (view and update profile)
    path('profile/', UserProfileView.as_view(), name='profile'),
]
