from .views import home
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('', include("library.urls")),
    path('', include("users.urls")),
]
