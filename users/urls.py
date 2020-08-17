"""Users URL Configuration."""
from django.urls import path

from .views import SignUpAPI, SignInAPI, profile_api, UserListAPI, UserPictureUpdateAPI, UserpasswordUpdateAPI

urlpatterns = [
    path("", UserListAPI.as_view()),
    path("signup/", SignUpAPI.as_view()),
    path("signin/", SignInAPI.as_view()),
    path("profile/", profile_api),
    path("profile/picture/", UserPictureUpdateAPI.as_view()),
    path("profile/password/", UserpasswordUpdateAPI.as_view()),
]
