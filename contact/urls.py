"""contact URL Configuration."""
from django.urls import path
from .views import ContactCreateAPI

urlpatterns = [
    path("", ContactCreateAPI.as_view())
]
