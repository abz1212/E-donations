from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from .serializers import UserSerializer, ProfileSerializer
from .models import CustomUser


class SignUpAPI(CreateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class SignInAPI(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'picture': user.picture.url,
        })


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def profile_api(request):
    serializer = ProfileSerializer(request.user)
    return Response(serializer.data)
