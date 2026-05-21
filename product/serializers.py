from drf_spectacular import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from yaml import serializer
from .models import Category, Book, BookImage


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

    class Meta:
        model = Book
        # fields = ['id', 'name', 'slug', 'price', 'book_image', 'category', 'info', 'author', 'views']
        fields = '__all__'

class BookCreateSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'name', 'slug', 'price', 'count', 'category', 'info', 'author']


class CategoryDetailSerializer(ModelSerializer):

    books = BookSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'category_image', 'books']
<<<<<<< HEAD
        
        
class BookDetailSerializer(serializer.ModelSerializer):
    category_name = serializer.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = ['id', 'name', 'slug', 'price', 'about', 'count', 'is_active', 'category_name', 'info', 'author', 'views']
        
        def get_category_name(self, obj):     
            return obj.category.name 
        
        
class CategoryDetailSerializer(serializers.ModelSerializer):
    books = BookDetailSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'category_image', 'books']
=======




class BookUpdateSerializer(ModelSerializer):
    book_image = BookImageSerializer(many=True)
    class Meta:
        model = Book
        fields = ['name', 'price', 'book_image', 'about', 'is_active']



>>>>>>> 8ef0e1980eb06ef74146f7a761dd94e5fd7b0795
