from rest_framework.serializers import ModelSerializer, Serializer

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




class BookUpdateSerializer(ModelSerializer):
    book_image = BookImageSerializer(many=True)
    class Meta:
        model = Book
        fields = ['name', 'price', 'book_image', 'about', 'is_active']
        read_only_fields = ['added_user']



