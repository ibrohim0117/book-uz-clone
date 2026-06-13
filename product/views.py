import django_filters
from rest_framework.generics import (
    CreateAPIView, ListAPIView,
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from rest_framework.authentication import BasicAuthentication
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import BookFilter

from .models import Author, Category, Book
from .serializers import (
    CategorySerializer, CategoryDetailSerializer,
    CategoryUpdateSerializer, BookSerializer, BookUpdateSerializer,
    BookCreateSerializer
)


@extend_schema(tags=['category'])
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, ]
    
    
class CategoryListCreateApiViuw(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, ]

    

@extend_schema(tags=['category/slug'])
class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategoryDetailSerializer
        
        elif self.request.method == "PUT":
            return CategoryUpdateSerializer
        
        else:
            return self.serializer_class
        
        
class BookPagination(PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'page-size'
    max_page_size = 1
    
    def get_paginated_response(self, data):
        return Response({
            'total_items': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'results': data
        })


@extend_schema(tags=['book'])
class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    pagination_class = BookPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = BookFilter
    search_fields = ['name', 'about']
    
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
        
        else:
            return self.serializer_class
        
        
# # mualif uchun bu
# class AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# # foydalanuvchi uchun profil api
# class UserProfileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer