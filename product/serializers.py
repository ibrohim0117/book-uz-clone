from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers



from .models import Category, Book, BookImage, Author



class CategorySerializer(ModelSerializer):
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

    


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"