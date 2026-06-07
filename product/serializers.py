from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers


from .models import Category, Book, BookImage, Author



class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'category_image', 'books']
        read_only_fields = ['id', 'slug', 'books']



class BookImageSerializer(ModelSerializer):
    class Meta:
        model = BookImage
        fields = ['id', 'image']



class BookSerializer(ModelSerializer):
    book_image = BookImageSerializer(many=True)
    name = serializers.CharField()

    class Meta:
        model = Book
        # fields = ['id', 'name', 'slug', 'price', 'book_image', 'category', 'info', 'author', 'views']
        fields = '__all__'
        read_only_fields = ['added_user', 'id', 'slug', 'views']



# class BookUpdateSerializer(ModelSerializer):
#     book_image = BookImageSerializer(many=True)
#     class Meta:
#         model = Book
#         fields = ['name', 'price', 'book_image', 'about', 'is_active']
#         read_only_fields = ['added_user']



class AuthorCreateSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"