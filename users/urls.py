from django.urls import path
from .views import home, users

urlpatterns = [
    path("users/home", home),
    path("users/social", users)
]