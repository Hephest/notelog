from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from jwtauth.serializers import UserCreateSerializer


class UserRegistrationView(CreateAPIView):
    """
    API endpoint that allows user to be created through
    simple registration process.
    """
    permission_classes = (AllowAny, )
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response(res, status.HTTP_201_CREATED)
