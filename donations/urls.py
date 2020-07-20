"""donations URL Configuration."""
from django.urls import path

from .views import BloodDonationRequestsCreateAPI, OrganDonationRequestsCreateAPI, MoneyDonationCreateAPI

urlpatterns = [

    path("blood/", BloodDonationRequestsCreateAPI.as_view()),

    path("oragn/", OrganDonationRequestsCreateAPI.as_view()),

    path("money/", MoneyDonationCreateAPI.as_view()),

]
