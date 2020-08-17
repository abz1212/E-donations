from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, GenericAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from django.shortcuts import get_object_or_404

from .serializers import UserSerializer, ProfileSerializer, UserListSerializer, UserPictureUpdateSerializer, UserChangePasswordSerializer
from .models import CustomUser


class SignUpAPI(CreateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class UserListAPI(ListAPIView):
    serializer_class = UserListSerializer
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


class UserPictureUpdateAPI(UpdateAPIView):
    serializer_class = UserPictureUpdateSerializer
    queryset = CustomUser.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        user = self.request.user
        obj = get_object_or_404(queryset, username=user.username)
        return obj


class UserpasswordUpdateAPI(GenericAPIView):
    serializer_class = UserChangePasswordSerializer
    queryset = CustomUser.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        user = self.request.user
        obj = get_object_or_404(queryset, username=user.username)
        return obj

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):

            old_password = serializer.data.get("old_password")

            new_password = serializer.data.get("new_password")

            retype_new_password = serializer.data.get("retype_new_password")

            success = request.user.check_password(old_password)

            if success and new_password == retype_new_password:
                request.user.set_password(new_password)

                request.user.save()

                return Response(
                    {"detail": "Your password has been changed"},
                    status=status.HTTP_201_CREATED,
                )
        else:
            return Response(
                {"detail": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )
