from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from .serializers import UserSerializer


class RegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        return ObtainAuthToken().post(request)


class LogoutView(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
