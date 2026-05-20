from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Category, Book, BookImage, Author


class BookImageSerializer(ModelSerializer):
    class Meta:
        model = BookImage
        fields = ['id', 'image']


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'full_name', 'about', 'created_at', 'updated_at']


class BookSerializer(ModelSerializer):
    book_image = BookImageSerializer(many=True, read_only=True)
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'slug', 'price', 'about', 'count', 'is_active', 
                  'book_image', 'category', 'info', 'author', 'views', 'created_at', 'updated_at']


class CategorySerializer(ModelSerializer):
    books = serializers.SerializerMethodField()

    def get_books(self, obj):
        class _BookInCategorySerializer(ModelSerializer):
            class Meta:
                model = Book
                fields = ['id', 'name', 'slug', 'price']

        qs = obj.books.all()
        return _BookInCategorySerializer(qs, many=True).data

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'category_image', 'books', 'created_at', 'updated_at']


class CategoryUpdateSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'category_image']


class CategoryDetailSerializer(ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'category_image', 'books', 'created_at', 'updated_at']