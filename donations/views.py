from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from .serializers import BloodDonationRequestsSerializer, OrganDonationRequestsSerializer, MoneyDonationSerializer
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
