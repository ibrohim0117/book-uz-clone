
from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView,
    ListCreateAPIView
)

from .permissions import IsAdminRoleUser
from rest_framework.authentication import BasicAuthentication
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import permissions
from drf_spectacular.utils import extend_schema
from .models import Category, Book
from .models import Category, Book, Author
from .serializers import (
    CategorySerializer,BookSerializer,
    AuthorCreateSerializer, CategoryDetailSerializer, CategoryUpdateSerializer,
    BookCreateSerializer, BookUpdateSerializer, 
)



@extend_schema(tags=['category'])
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]  


@extend_schema(tags=['category'])
class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [BasicAuthentication] 
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser] 


@extend_schema(tags=['category/slug'])
class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategoryDetailSerializer
        elif self.request.method in ["PUT", "PATCH"]:
            return CategoryUpdateSerializer
        return CategoryDetailSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

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
class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [permissions.AllowAny] 


@extend_schema(tags=['book'])
class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
    authentication_classes = [BasicAuthentication]  
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]  

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

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
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookSerializer
        elif self.request.method in ["PUT", "PATCH"]:
            return BookUpdateSerializer
        return BookSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


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

