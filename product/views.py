from rest_framework.generics import (
    CreateAPIView, ListAPIView,
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Book
from .serializers import (
    CategorySerializer, CategoryDetailSerializer,
    CategoryUpdateSerializer, BookSerializer, BookUpdateSerializer
)



class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'slug'

    def get_serializer(self, *args, **kwargs):

        if self.request.method == "PUT":
            serializer = CategoryUpdateSerializer(data=self.request.data)
            
            if serializer.is_valid():
                serializer.save()

                return Response(
                    status=status.HTTP_200_OK,
                    data=serializer.data
                )
                
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )
    
        elif self.request.method == "DELETE":

            category = Category.objects.filter(slug=self.kwargs['slug']).first()
            category.delete()

            return Response(
                status=status.HTTP_204_NO_CONTENT
            )
            
        
        elif self.request.method == "GET":
            category_obj = Category.objects.filter(slug=self.kwargs['slug']).first()
            serializer = CategoryDetailSerializer(category_obj)

            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )

        return super().get_serializer(*args, **kwargs)



class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'

    def get_serializer(self, *args, **kwargs):

        if self.request.method == "PUT":
            serializer = BookUpdateSerializer(data=self.request.data)
            
            if serializer.is_valid():
                serializer.save()

                return Response(
                    status=status.HTTP_200_OK,
                    data=serializer.data
                )
                
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )
    
        elif self.request.method == "DELETE":

            category = Book.objects.filter(slug=self.kwargs['slug']).first()
            category.delete()

            return Response(
                status=status.HTTP_204_NO_CONTENT
            )
            
        
        elif self.request.method == "GET":
            category_obj = Book.objects.filter(slug=self.kwargs['slug']).first()
            serializer = BookSerializer(category_obj)

            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )

        return super().get_serializer(*args, **kwargs)