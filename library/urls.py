from django.urls import path
from .views import home, books

urlpatterns = [
    path("library/home/", home),
    path("library/books/", books)
]
