from itertools import chain

from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BloodDonationRequestsSerializer, OrganDonationRequestsSerializer, MoneyDonationSerializer, \
    RecentDonorsSerializer
from .models import Blood, Sponsor, Organ


class BloodDonationRequestsCreateAPI(CreateAPIView):
    serializer_class = BloodDonationRequestsSerializer
    queryset = Blood.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(donor=self.request.user)


class OrganDonationRequestsCreateAPI(CreateAPIView):
    serializer_class = OrganDonationRequestsSerializer
    queryset = Organ.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(donor=self.request.user)


class MoneyDonationCreateAPI(CreateAPIView):
    serializer_class = MoneyDonationSerializer
    queryset = Sponsor.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(donor=self.request.user)


@api_view(["GET"])
def recent_donors(request):
    bloods = Blood.objects.all().order_by("-created_at")[:2]

    organs = Organ.objects.all().order_by("-created_at")[:2]

    sponsors = Sponsor.objects.all().order_by("-created_at")[:2]

    qs = list(chain(bloods, organs, sponsors))

    serializer = RecentDonorsSerializer(qs, many=True)

    return Response(serializer.data)
