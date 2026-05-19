from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Category
from .serializers import CategorySerializer, CategoryDetailSerializer, CategoryUpdateSerializer



class CategoryListCreateAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CategoryDetailUpdateDeleteAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        serializer = CategoryUpdateSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        category.delete()
        return Response(
            {"message": "Kategoriya muvaffaqiyatli o'chirildi"}, 
            status=status.HTTP_200_OK
        )