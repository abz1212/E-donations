from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer
from .models import CustomUser


class SignUpAPI(CreateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
