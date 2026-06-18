
from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView,
    ListCreateAPIView
)

from .permissions import IsAdminRoleUser
from rest_framework.authentication import BasicAuthentication

from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import permissions
from django.db.models import F

from .models import Category, Book, Author
from users.models import Users
from .serializers import (
    CategorySerializer,BookSerializer,
    AuthorSerializer
)
from .filters import FilterMaxMinValue
from .permissions import IsAdminRoleUser




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
    permission_classes = [permissions.AllowAny] 


# @extend_schema(tags=['book'])
# class BookCreateAPIView(CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookCreateSerializer
#     authentication_classes = [BasicAuthentication]  
#     permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]  

#     def perform_create(self, serializer):
#         serializer.save(added_by=self.request.user)

#     filterset_fields = ['price', ]
#     filterset_class = FilterMaxMinValue
    
#     # def get_queryset(self):
#     #     queryset = Book.objects.all()
#     #     search_query = self.request.query_params.get('search', None)

#     #     if search_query:
#     #         queryset = Book.objects.filter(name__icontains=search_query)


#     #     return queryset 

#     def get_permissions(self):
#         if self.request.method == "GET":
#             return [AllowAny(), ]
#         return [IsAuthenticated(), IsAdminRoleUser()]
    
    
#     def perform_create(self, serializer):
#         return serializer.save(add_user=self.request.user)



@extend_schema(tags=['book/slug'])
class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'

    # def get_serializer_class(self):
    #     if self.request.method == 'GET':
    #         return BookSerializer
    #     elif self.request.method in ["PUT", "PATCH"]:
    #         return BookUpdateSerializer
    #     return BookSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


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
    

class AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer




@extend_schema(tags=["author-get-put-delete"])
class AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        return [IsAuthenticated(), IsAdminRoleUser()]
    