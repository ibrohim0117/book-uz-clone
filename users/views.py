from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_spectacular.utils import extend_schema

from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .serializers import UserRegisterSerializer, UserProfileSerializer, SocialNetworkSerializer
from rest_framework.exceptions import PermissionDenied
from .models import Users, SocialNetwork



@extend_schema(tags=['Register'])
class RegisterCreateAPIView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserRegisterSerializer

    


@extend_schema(tags=["Profile"])
class UserProfileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserProfileSerializer

    def get_permissions(self):
        return [IsAuthenticated()]

    def perform_update(self, serializer):
        instance = self.get_object()
        if self.request.user != instance and not self.request.user.is_staff:
            raise PermissionDenied("Not permitted to edit this profile.")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user != instance and not self.request.user.is_staff:
            raise PermissionDenied("Not permitted to delete this profile.")
        instance.delete()


@extend_schema(tags=["SocialNetwork"])
class SocialNetworkListCreateAPIView(ListCreateAPIView):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=["SocialNetwork"])
class SocialNetworkRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer

    def get_permissions(self):
        return [IsAuthenticated()]

    def perform_destroy(self, instance):
        if instance.user != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied("Not permitted to delete this social account.")
        instance.delete()


