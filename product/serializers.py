from rest_framework.serializers import ModelSerializer
from .models import Category, Book, BookImage
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Category, Book, BookImage, Author
from users.models import Users




class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'category_image']


class CategoryUpdateSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'category_image', 'books', 'parent']
        read_only_fields = ['id', 'slug', 'books']


class BookImageSerializer(ModelSerializer):
    class Meta:
        model = BookImage
        fields = ['id', 'image']


class BookSerializer(ModelSerializer):
    book_image = BookImageSerializer(many=True, read_only=True)
    name = serializers.CharField()

    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['add_user', 'id', 'slug', 'views']


class BookCreateSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'slug', 'price', 'count', 'category', 'info', 'author', 'added_by']
        read_only_fields = ['added_by', 'slug']


class CategoryDetailSerializer(ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'category_image', 'books']


class BookUpdateSerializer(ModelSerializer):
    book_image = BookImageSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ['name', 'price', 'book_image', 'about', 'is_active']




class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'  


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
