from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Users, SocialNetwork

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        style={'input_type': 'password'}
    )

    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'phone_number', 'password']
        extra_kwargs = {
            'email': {'required': True}, # Email kiritishni majburiy qilamiz
        }

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
      
        user = Users.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number', None) 
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'phone_number', 'created_at', 'is_staff']
        read_only_fields = ['id', 'created_at', 'is_staff'] 
from rest_framework import serializers 
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password

from .models import Users



class UserRegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = Users
        fields = ["first_name", "username", "password"]

    def validate_password(self, password):
        return make_password(password)
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update(instance.token())
        return data 


class SocialNetworkSerializer(ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ["id", "title", "url", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]