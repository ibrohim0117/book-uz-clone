from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'password']
        extra_kwargs = {
            'email': {'required': True}, # Email kiritishni majburiy qilamiz
        }

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
      
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number', None) 
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'created_at', 'is_staff']
        read_only_fields = ['id', 'created_at', 'is_staff'] 
from rest_framework import serializers 
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password

from .models import Users


class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    role = serializers.CharField(read_only=True)

    class Meta:
        model = Users
        fields = [
            'first_name', 'last_name',
            "username", 'password', 'phone', 'about', 
            'role'
        ]


    def validate_password(self, password):
        return make_password(password)
