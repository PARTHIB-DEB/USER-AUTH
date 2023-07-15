from django.urls import path, include
from rest_framework.routers import DefaultRouter
from APP import api_views

# Create a router and register our viewsets with it.

my_router = DefaultRouter()
my_router.register(r'', api_views.UserViewSet, basename="user_details")

# The API URLs are now determined automatically by the router.

urlpatterns = [
    
    path('', api_views.UserViewSet.as_view()),
    
]
