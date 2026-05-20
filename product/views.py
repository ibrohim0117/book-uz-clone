from rest_framework.generics import (
    CreateAPIView, ListAPIView,
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework import status

from .models import Category, Book
from .serializers import (
    CategorySerializer, CategoryDetailSerializer,
    CategoryUpdateSerializer
)


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return CategoryUpdateSerializer
        return CategoryDetailSerializer
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        detail_serializer = CategoryDetailSerializer(instance)
        return Response(detail_serializer.data)
