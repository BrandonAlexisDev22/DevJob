from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserReadSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self,requests):
        serializer = RegisterSerializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        serializer.create()
        user = serializer.save()
        user_data = UserReadSerializer(user).data
        return Response (
            {
                "message": "Usuario Registrado",
                "User": user_data,
            },
            status = status.HTTP_201_CREATED
        )