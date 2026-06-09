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
