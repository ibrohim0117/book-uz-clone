from rest_framework.generics import (
    CreateAPIView, ListAPIView,
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets

from .models import Category, Book
from .serializers import (
    CategorySerializer, CategoryDetailSerializer,
    CategoryUpdateSerializer, BookSerializer, BookUpdateSerializer,
    BookCreateSerializer
)


@extend_schema(tags=['category'])
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

@extend_schema(tags=['category/slug'])
class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'slug'
<<<<<<< HEAD
    
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
=======

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategoryDetailSerializer
        
        elif self.request.method == "PUT":
            return CategoryUpdateSerializer


@extend_schema(tags=['book'])
class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookSerializer
        
        elif self.request.method == "POST":
            return BookCreateSerializer
        

@extend_schema(tags=['book/slug'])
class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookSerializer
        
        elif self.request.method == "PUT":
            return BookUpdateSerializer
>>>>>>> 8ef0e1980eb06ef74146f7a761dd94e5fd7b0795
