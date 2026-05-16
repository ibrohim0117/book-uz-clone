from django.shortcuts import render

<<<<<<< HEAD
# create your view here/
=======
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
>>>>>>> 362cccfb11de155287a29a943e77a732bad3fcdf
