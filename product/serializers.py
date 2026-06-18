from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers


from .models import Category, Book, BookImage, Author



class CategorySerializer(ModelSerializer):
    parent = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='slug', allow_null=True, required=False)
    children = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'category_image', 'parent', 'children', 'books']
        read_only_fields = ['id', 'slug', 'children', 'books']



class BookImageSerializer(ModelSerializer):
    class Meta:
        model = BookImage
        fields = ['id', 'image']



class BookSerializer(ModelSerializer):
    book_image = BookImageSerializer(many=True, read_only=True)
    name = serializers.CharField()

    class Meta:
        model = Book
        # fields = ['id', 'name', 'slug', 'price', 'book_image', 'category', 'info', 'author', 'views']
        fields = '__all__'
        read_only_fields = ['add_user', 'id', 'slug', 'views']




class AuthorCreateSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"