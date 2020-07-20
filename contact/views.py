from rest_framework.generics import CreateAPIView
from .serializers import ContactSerializer
from .models import Contact


class ContactCreateAPI(CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
