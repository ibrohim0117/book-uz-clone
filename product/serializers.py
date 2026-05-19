from rest_framework import serializers
from .models import Category, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'slug', 'price', 'about', 'count', 'is_active', 'views', 'info']

    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'parent', 'category_image', 'created_at', 'updated_at']
        read_only_fields = ['slug', 'created_at', 'updated_at']


class CategoryDetailSerializer(serializers.ModelSerializer):
    books = BookSerializer(source='category', many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'parent', 'category_image', 'created_at', 'updated_at', 'books']


class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'category_image'] 