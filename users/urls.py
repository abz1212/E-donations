"""Users URL Configuration."""
from django.urls import path
from rest_framework.authtoken import views

from .views import SignUpAPI

urlpatterns = [
    path("signup/", SignUpAPI.as_view()),
    path("signin/", views.obtain_auth_token)
]
