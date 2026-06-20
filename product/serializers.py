from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers



from .models import Category, Book, BookImage, Author



class CategorySerializer(ModelSerializer):
    parent_name = serializers.CharField(source='parent.name', read_only=True, default=None)

    class Meta:
        model = Category
        # 'books' (kitoblar id ro'yxati) olib tashlandi - TODO item 4.
        # parent_name qo'shildi - TODO item 5.
        fields = ['id', 'name', 'slug', 'category_image', 'parent', 'parent_name']
        read_only_fields = ['id', 'slug']



class BookImageSerializer(ModelSerializer):
    class Meta:
        model = BookImage
        fields = ['id', 'image']



class BookSerializer(ModelSerializer):
    book_image = BookImageSerializer(many=True, read_only=True)
    name = serializers.CharField()
    # category bo'yicha id va name ham kelishi kerak - TODO item 3
    category_name = serializers.CharField(source='category.name', read_only=True, default=None)

    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['add_user', 'id', 'slug', 'views']

    


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"