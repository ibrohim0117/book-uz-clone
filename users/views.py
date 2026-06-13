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
from .serializers import UserRegisterSerializer, UserProfileSerializer
from rest_framework.exceptions import PermissionDenied
from .models import Users



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

