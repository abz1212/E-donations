"""Users URL Configuration."""
from django.urls import path
from rest_framework.authtoken import views

from .views import SignUpAPI, SignInAPI, profile_api

urlpatterns = [
    path("signup/", SignUpAPI.as_view()),
    path("signin/", SignInAPI.as_view()),
    path("profile/", profile_api)
]
