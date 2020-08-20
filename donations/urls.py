"""donations URL Configuration."""
from django.urls import path

from .views import BloodDonationRequestsCreateAPI, OrganDonationRequestsCreateAPI, MoneyDonationCreateAPI, recent_donors, AcceptorAPI

urlpatterns = [

    path("blood/", BloodDonationRequestsCreateAPI.as_view()),

    path("organ/", OrganDonationRequestsCreateAPI.as_view()),

    path("money/", MoneyDonationCreateAPI.as_view()),

    path("recent/", recent_donors),

    path("acceptor/", AcceptorAPI.as_view()),

]
