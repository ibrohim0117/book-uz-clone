from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.authentication import  JWTAuthentication

from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView
)

from .serializers import UserRegisterSerializer, UserProfileSerializer
from .models import Users


<<<<<<< HEAD
    authentication_classes = [BasicAuthentication]


    def get(self, request, format=None):
        content = {
            'user': str(request.user), 
            'auth': str(request.auth), 
        }
        return Response(content)
    
=======
>>>>>>> 2eac412907f0c695ee4122923a99df85ae5e7602

@extend_schema(tags=['Register'])
class RegisterCreateAPIView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserRegisterSerializer

    
@extend_schema(tags=['User/Profile'])
class ProfileRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserProfileSerializer
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user