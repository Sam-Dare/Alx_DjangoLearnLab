from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookViewSet, BookList

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# Define URL patterns
urlpatterns = [
    # Existing list view (optional)
    path('books/', BookList.as_view(), name='book-list'),
    # Include router-generated URLs
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]
