from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        style={'input_type': 'password'}
    )

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number', 'password']
        extra_kwargs = {
            'email': {'required': True}, # Email kiritishni majburiy qilamiz
        }

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
      
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number', None) 
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number', 'created_at', 'is_staff']
        read_only_fields = ['id', 'created_at', 'is_staff'] 