from django.shortcuts import render

from rest_framework.generics import (
    CreateAPIView, ListAPIView,
    ListCreateAPIView, RetrieveAPIView,
    DestroyAPIView, UpdateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .models import Category, Book
from .serializers import CategorySerializer



class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
