from rest_framework.generics import (
    CreateAPIView, ListAPIView,
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Category, Book, Author
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
    filterset_class = FilterMaxMinValue
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'about', 'author__full_name', 'category__name']
    ordering_fields = ['price', 'views', 'created_at']
    ordering = ['-created_at']
        

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        return [IsAuthenticated(), IsAdminRoleUser()]
    
    
    def perform_create(self, serializer):
        return serializer.save(add_user=self.request.user)



    # def get_queryset(self):
    #     queryset = Book.objects.all()
    #     search_query = self.request.query_params.get('search', None)

    #     if search_query:
    #         queryset = Book.objects.filter(name__icontains=search_query)


    #     return queryset 



@extend_schema(tags=['book/slug'])
class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        return [IsAdminRoleUser(), IsAuthenticated()]


        
@extend_schema(tags=["Author"])
class AuthorCreateApiView(ListCreateAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = None

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        return [IsAuthenticated(), IsAdminRoleUser()]
    

    def perform_create(self, serializer):
        return serializer.save(add_user=self.request.user)
    


@extend_schema(tags=["Author/slug"])
class AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        return [IsAuthenticated(), IsAdminRoleUser()]