from rest_framework.generics import (
    CreateAPIView, ListAPIView,
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import permissions
from django.db.models import F

from .models import Category, Book, Author
from .serializers import (
    CategorySerializer,BookSerializer,
    AuthorSerializer, BookDetailSerializer,
    CategoryDetailSerializer
)
from .filters import FilterMaxMinValue
from .permissions import IsAdminRoleUser




@extend_schema(tags=['category'])
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #parent filtr ni qoshtim
    filterset_fields = ['parent']

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsAdminRoleUser()]
        
        return [AllowAny()]
    
    
    
@extend_schema(tags=['category/slug'])
class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
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
    filterset_fields = ['category']

    

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
    serializer_class = BookDetailSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        return [IsAdminRoleUser(), IsAuthenticated()]


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Book.objects.filter(pk=instance.pk).update(views=F('views') + 1)
        instance.views += 1
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    
    
@extend_schema(tags=["author-get-post"])
class AuthorCreateApiView(ListCreateAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        return [IsAuthenticated(), IsAdminRoleUser()]
    

    def perform_create(self, serializer):
        return serializer.save(add_user=self.request.user)
    


@extend_schema(tags=["author-get-put-delete"])
class AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        return [IsAuthenticated(), IsAdminRoleUser()]
    