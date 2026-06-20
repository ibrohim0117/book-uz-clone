from rest_framework import serializers
from .models import Category, Book, BookImage
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers



from .models import Category, Book, BookImage, Author



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # don't expose related book ids in category list
        fields = ['id', 'name', 'slug', 'category_image']


class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'category_image']


class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImage
        fields = ['id', 'image']
        
        
class CategoryMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class BookSerializer(ModelSerializer):
    book_image = BookImageSerializer(many=True, read_only=True)
    name = serializers.CharField()
    category = CategoryMinimalSerializer(read_only=True)  # manashuni qoshtim!

    class Meta:
        model = Book
        fields = '__all__'  
        read_only_fields = ['add_user', 'id', 'slug', 'views']


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'slug', 'price', 'count', 'category', 'info', 'author']
        read_only_fields = ['added_by']


class BookDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    category = CategoryMinimalSerializer(read_only=True)
    
    class Meta:
        model = Book
        fields = [
            'id', 'name', 'slug', 'price', 'about', 'count', 
            'is_active', 'category_name', 'info', 'author', 'views',
            'category'
        ]
        
    def get_category_name(self, obj):     
        if obj.category:
            return obj.category.name 
        return None


class CategoryDetailSerializer(serializers.ModelSerializer):
    books = BookDetailSerializer(many=True, read_only=True)
    parent_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'category_image', 'parent_name', 'books']

    def get_parent_name(self, obj):
        if obj.parent:
            return obj.parent.name
        return None


class BookUpdateSerializer(serializers.ModelSerializer):
    book_image = BookImageSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['name', 'price', 'book_image', 'about', 'is_active']


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
        read_only_fields = ['add_user']
