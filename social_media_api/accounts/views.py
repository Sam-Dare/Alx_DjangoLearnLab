from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CustomUser
from .serializers import UserSerializer, UserRegistrationSerializer, UserLoginSerializer

class FollowUserView(generics.GenericAPIView):
    """
    Allows authenticated users to follow other users.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        # Get the user to follow
        user_to_follow = get_object_or_404(CustomUser.objects.all(), id=user_id)
        
        # Prevent following oneself
        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user is already following
        if request.user.following.filter(id=user_id).exists():
            return Response({"message": "You are already following this user."}, status=status.HTTP_200_OK)

        # Add to following list
        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}."}, status=status.HTTP_201_CREATED)

class UnfollowUserView(generics.GenericAPIView):
    """
    Allows authenticated users to unfollow other users.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        # Get the user to unfollow
        user_to_unfollow = get_object_or_404(CustomUser.objects.all(), id=user_id)

        # Check if the user is currently following
        if not request.user.following.filter(id=user_id).exists():
            return Response({"error": "You are not following this user."}, status=status.HTTP_400_BAD_REQUEST)

        # Remove from following list
        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)

class RegisterView(generics.GenericAPIView):
    """
    Allows users to register an account.
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegistrationSerializer  # Explicitly set the serializer class

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  # Use self.get_serializer
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(generics.GenericAPIView):
    """
    Allows authenticated users to view and update their profiles.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Get the current authenticated user
        user = request.user
        # Serialize the user data
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        user = request.user
        data = request.data.copy()

        # Prevent modification of followers directly
        data.pop('followers', None)
        
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    """
    Allows users to log in and obtain a token.
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer  # Explicitly set the serializer class here

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  # Uses UserLoginSerializer
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key})
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
