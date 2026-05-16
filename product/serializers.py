from rest_framework.serializers import ModelSerializer, Serializer

from .models import Category, Book


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'category_image']