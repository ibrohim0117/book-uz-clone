from rest_framework import serializers 
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from .validation import validate_phone_number, validate_https_url
from django.utils.text import slugify


from .models import Users, SocialNetwork, Cart
from product.models import Book



class UserRegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = Users
        fields = ["first_name", "username", "password", "phone"]


    def validate_password(self, password):
        return make_password(password)
    

    def validate(self, attrs):
        if not validate_phone_number(attrs['phone']):
            raise serializers.ValidationError("Telefon raqam formati xato!")
        return super().validate(attrs)
    

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update(instance.token())
        return data


class SocialAccountListSerializer(ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = '__all__'



class SocialAccountSerializer(ModelSerializer):

    class Meta:
        model = SocialNetwork
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at', 'uuid', 'user']

        
    def validate(self, attrs):
        url = attrs.get('url')
        title = attrs.get('title')

        if not validate_https_url(url):
            raise serializers.ValidationError({"url": "Sahifa formati xato!, https:// bo'lishi shart!"})

        if title:
            attrs['title'] = title.strip().lower().replace(' ', '-')

        return super().validate(attrs)

# Instagram sahifam -> instagram-saifam
        



class UserProfileSerializer(ModelSerializer):
    social_acc_list = SocialAccountSerializer(many=True)

    class Meta:
        model = Users
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = ['username', 'social_acc_list']


class UserCartSerializer(ModelSerializer):

    class Meta:
        model = Cart
        fields = "__all__"

    def validate(self, attrs):
        book = attrs.get('book')
        count = attrs.get('count')

        if book.count < count:
            raise serializers.ValidationError("Omborda kitob yetarli emas!")

        return super().validate(attrs)