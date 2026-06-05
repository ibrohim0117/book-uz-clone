from rest_framework.generics import (
    CreateAPIView, ListAPIView,
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from rest_framework.authentication import BasicAuthentication

from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import permissions

from .models import Category, Book, Author
from .serializers import (
    CategorySerializer, CategoryDetailSerializer,
    CategoryUpdateSerializer, BookSerializer, BookUpdateSerializer,
    BookCreateSerializer, AuthorCreateSerializer
)


@extend_schema(tags=['category'])
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):

        if self.request.method == "POST":
            return [IsAuthenticated(), IsAdminUser()]
        
        return [AllowAny()]
    
    
    

@extend_schema(tags=['category/slug'])
class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]            
        return [IsAdminUser(), IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategoryDetailSerializer
        
        elif self.request.method == "PUT":
            return CategoryUpdateSerializer
        
        else:
            return self.serializer_class


@extend_schema(tags=['book'])
class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        return [IsAdminUser(), IsAuthenticated()]
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookSerializer
        
        elif self.request.method == "POST":
            return BookCreateSerializer
        
    def perform_create(self, serializer):
        return serializer.save(added_user=self.request.user)
        

@extend_schema(tags=['book/slug'])
class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        return [IsAdminUser(), IsAuthenticated()]


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookSerializer
        
        elif self.request.method == "PUT":
            return BookUpdateSerializer

        
        else:
            return self.serializer_class
        

@extend_schema(tags=["Author"])
class AuthorCreateApiView(ListCreateAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorCreateSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny, ]
        return [IsAuthenticated, IsAdminUser]