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
            "username", 'password', 'phone',  
            'role'
        ]


    def validate_password(self, password):
        return make_password(password)