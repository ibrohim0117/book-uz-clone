from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.authentication import  JWTAuthentication
from product.permissions import IsAdminRoleUser

from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView,
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from .serializers import (
    UserRegisterSerializer, 
    UserProfileSerializer, 
    SocialAccountSerializer
)
from .models import Users, SocialNetwork



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


@extend_schema(tags=['User/SocialNetwork'])
class SocialNetworkListCreateAPIView(ListCreateAPIView):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialAccountSerializer
    # filterset_fields = ['title']
    pagination_class = None
    
    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        return [IsAuthenticated(), IsAdminRoleUser()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=['User/SocialNetwork'])
class SocialNetworkRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialAccountSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return SocialNetwork.objects.filter(user=self.request.user)

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]            
        return [IsAuthenticated(), IsAdminRoleUser()]