from rest_framework.generics import (
    CreateAPIView, ListAPIView,
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from rest_framework.authentication import BasicAuthentication
from rest_framework import permissions
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework import status
from rest_framework import permissions

from .models import Category, Book
from .serializers import (
    CategorySerializer, CategoryDetailSerializer,
    CategoryUpdateSerializer, BookSerializer, BookUpdateSerializer,
    BookCreateSerializer
)

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import IsAdminRoleUser


@extend_schema(tags=['category'])
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated, ]
    def get_permissions(self):
        if self.request.method == 'POST':
            return[permissions.IsAuthenticated(), permissions.IsAdminUser()]
        return[permissions.AllowAny()]
  

@extend_schema(tags=['category/slug'])
class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'slug'
    
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return[permissions.IsAdminUser()]
        return[permissions.AllowAny()]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

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
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookSerializer
        
        elif self.request.method == "POST":
            return BookCreateSerializer
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return[IsAuthenticated(), IsAdminRoleUser()]
        return[permissions.AllowAny()]
    
    #adminni avtomatik saqlaydi useerdan ustoz!
    def perform_create(self, serializer):
        serializer.save(add_user=self.request.user)


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
        
        else:
            return self.serializer_class
        
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
