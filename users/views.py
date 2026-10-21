from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserReadSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_data = UserReadSerializer(user).data
        return Response (
            {
                "message": "Usuario Registrado",
                "user": user_data,
            },
            status = status.HTTP_201_CREATED
        )