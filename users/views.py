from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_spectacular.utils import extend_schema

from rest_framework.generics import (
    CreateAPIView, ListAPIView
)

from .serializers import RegisterSerializer
from .models import Users

@extend_schema(tags=['Login'])
class Login(APIView):

    authentication_classes = [BasicAuthentication]


    def get(self, request, format=None):
        content = {
            'user': str(request.user), 
            'auth': str(request.auth), 
        }
        return Response(content)
    

@extend_schema(tags=['Register'])
class RegisterCreateAPIView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = RegisterSerializer
    