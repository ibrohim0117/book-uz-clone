from rest_framework.generics import (
    CreateAPIView, ListAPIView,
    ListCreateAPIView
)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Book
from .serializers import CategorySerializer, CategoryDetailSerializer, CategoryUpdateSerializer



class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



@api_view(['GET', 'PUT', 'DELETE'])
def get_category_detail(request, slug):
    if request.method == 'GET':

        category_obj = Category.objects.filter(slug=slug).all()


        serializer = CategoryDetailSerializer(category_obj, many=True)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
    elif request.method == 'PUT':

        serializer = CategoryUpdateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
    
    elif request.method == 'DELETE':
        try:
            category = Category.objects.filter(slug=slug).first()
            category.delete()

            return Response(
                status=status.HTTP_204_NO_CONTENT
            )
        except:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        



