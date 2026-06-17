<<<<<<< HEAD
from rest_framework import serializers
from .models import Category, Book, BookImage
=======
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers


from .models import Category, Book, BookImage, Author

>>>>>>> 2eac412907f0c695ee4122923a99df85ae5e7602


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
<<<<<<< HEAD
        fields = ['id', 'name', 'slug', 'category_image']


class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'category_image']

=======
        fields = ['id', 'name', 'slug', 'category_image', 'books', 'parent']
        read_only_fields = ['id', 'slug', 'books']
>>>>>>> 2eac412907f0c695ee4122923a99df85ae5e7602

class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImage
        fields = ['id', 'image']


<<<<<<< HEAD
class BookSerializer(serializers.ModelSerializer):
    book_image = BookImageSerializer(many=True, read_only=True)
=======

class BookSerializer(ModelSerializer):
    book_image = BookImageSerializer(many=True, read_only=True)
    name = serializers.CharField()
>>>>>>> 2eac412907f0c695ee4122923a99df85ae5e7602

    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['add_user', 'id', 'slug', 'views']


<<<<<<< HEAD
class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'slug', 'price', 'count', 'category', 'info', 'author']
        read_only_fields = ['added_by']


class BookDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = [
            'id', 'name', 'slug', 'price', 'about', 'count', 
            'is_active', 'category_name', 'info', 'author', 'views'
        ]
        
    def get_category_name(self, obj):     
        if obj.category:
            return obj.category.name 
        return None


class CategoryDetailSerializer(serializers.ModelSerializer):
    books = BookDetailSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'category_image', 'books']


class BookUpdateSerializer(serializers.ModelSerializer):
    book_image = BookImageSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['name', 'price', 'book_image', 'about', 'is_active']
=======


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
>>>>>>> 2eac412907f0c695ee4122923a99df85ae5e7602
