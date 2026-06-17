import django_filters
from rest_framework.generics import (
    CreateAPIView, ListAPIView,
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
<<<<<<< HEAD

from rest_framework.authentication import BasicAuthentication
=======
>>>>>>> 2eac412907f0c695ee4122923a99df85ae5e7602
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import BookFilter

<<<<<<< HEAD
from .models import Author, Category, Book
=======
from .models import Category, Book, Author
>>>>>>> 2eac412907f0c695ee4122923a99df85ae5e7602
from .serializers import (
    CategorySerializer,BookSerializer,
    AuthorSerializer
)
from .filters import FilterMaxMinValue
from .permissions import IsAdminRoleUser




@extend_schema(tags=['category'])
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
<<<<<<< HEAD
    permission_classes = [permissions.IsAuthenticated, ]
    
    
class CategoryListCreateApiViuw(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, ]
=======
    filterset_fields = ['name', ]
>>>>>>> 2eac412907f0c695ee4122923a99df85ae5e7602

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsAdminRoleUser()]
        
        return [AllowAny()]
    
    
    
@extend_schema(tags=['category/slug'])
class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

<<<<<<< HEAD
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
=======
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]            
        return [IsAuthenticated(), IsAdminRoleUser()]
>>>>>>> 2eac412907f0c695ee4122923a99df85ae5e7602

    

@extend_schema(tags=['book'])
class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = FilterMaxMinValue
    
<<<<<<< HEAD
    pagination_class = BookPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = BookFilter
    search_fields = ['name', 'about']
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookSerializer
        
        elif self.request.method == "POST":
            return BookCreateSerializer
    
=======
    # def get_queryset(self):
    #     queryset = Book.objects.all()
    #     search_query = self.request.query_params.get('search', None)

    #     if search_query:
    #         queryset = Book.objects.filter(name__icontains=search_query)


    #     return queryset 

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        return [IsAuthenticated(), IsAdminRoleUser()]
    
    
    def perform_create(self, serializer):
        return serializer.save(add_user=self.request.user)


>>>>>>> 2eac412907f0c695ee4122923a99df85ae5e7602

@extend_schema(tags=['book/slug'])
class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        return [IsAdminRoleUser(), IsAuthenticated()]


        
<<<<<<< HEAD
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
=======
@extend_schema(tags=["Author"])
class AuthorCreateApiView(ListCreateAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        return [IsAuthenticated(), IsAdminRoleUser()]
    

    def perform_create(self, serializer):
        return serializer.save(added_user=self.request.user)
    


@extend_schema(tags=["Author/slug"])
class AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        return [IsAuthenticated(), IsAdminRoleUser()]
    
    
    

    
>>>>>>> 2eac412907f0c695ee4122923a99df85ae5e7602
