from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers

from .models import Category, Book, BookImage, Author



class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'category_image']



class CategoryUpdateSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'category_image']



class BookImageSerializer(ModelSerializer):
    class Meta:
        model = BookImage
        fields = ['id', 'image']



class BookSerializer(ModelSerializer):
    book_image = BookImageSerializer(many=True)
    name = serializers.CharField()

    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['add_user', 'id', 'slug', 'views']


class BookCreateSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'slug', 'price', 'count', 'category', 'info', 'author']


class CategoryDetailSerializer(ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'category_image', 'books']



class BookUpdateSerializer(ModelSerializer):
    book_image = BookImageSerializer(many=True)
    class Meta:
        model = Book
        fields = ['name', 'price', 'book_image', 'about', 'is_active']
        read_only_fields = ['add_user']


class AuthorCreateSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
