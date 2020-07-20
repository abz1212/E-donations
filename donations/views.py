from rest_framework.generics import CreateAPIView

from .serializers import BloodDonationRequestsSerializer, OrganDonationRequestsSerializer, MoneyDonationSerializer
from .models import Request, Sponsor


class BloodDonationRequestsCreateAPI(CreateAPIView):
    serializer_class = BloodDonationRequestsSerializer
    queryset = Request.objects.all()


class OrganDonationRequestsCreateAPI(CreateAPIView):
    serializer_class = OrganDonationRequestsSerializer
    queryset = Request.objects.all()


class MoneyDonationCreateAPI(CreateAPIView):
    serializer_class = MoneyDonationSerializer
    queryset = Sponsor.objects.all()
