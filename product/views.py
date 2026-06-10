from rest_framework.generics import (
    CreateAPIView, ListAPIView,
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from .permissions import IsAdminRoleUser

from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import permissions

from .models import Category, Book, Author
from .serializers import (
    CategorySerializer,BookSerializer,
    AuthorCreateSerializer
)



@extend_schema(tags=['category'])
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['name', ]

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsAdminRoleUser()]
        
        return [AllowAny()]
    
    
    
@extend_schema(tags=['category/slug'])
class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]            
        return [IsAuthenticated(), IsAdminRoleUser()]

    

@extend_schema(tags=['book'])
class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_fields = ['price', ]

    def get_queryset(self):
        queryset = Book.objects.all()
        search_query = self.request.query_params.get('search', None)
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)

        if search_query:
            queryset = Book.objects.filter(name__icontains=search_query)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

            #tips __gte (Greater than or equal to - katta yoki teng) va __lte (Less than or equal to - kichik yoki teng)
        return queryset 

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        return [IsAuthenticated(), IsAdminRoleUser()]
    
    
    def perform_create(self, serializer):
        return serializer.save(add_user=self.request.user)



@extend_schema(tags=['book/slug'])
class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        return [IsAdminUser(), IsAuthenticated()]


        
@extend_schema(tags=["Author"])
class AuthorCreateApiView(ListCreateAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorCreateSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        return [IsAuthenticated(), IsAdminUser()]
    

    def perform_create(self, serializer):
        return serializer.save(added_user=self.request.user)