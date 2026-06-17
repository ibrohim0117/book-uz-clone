from rest_framework import serializers 
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password

from .models import Users, SocialNetwork



class UserRegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = Users
        fields = [
            'first_name', 'last_name',
            "username", 'password', 'phone', 'about', 
            'role'
        ]


    def validate_password(self, password):
        return make_password(password)
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update(instance.token())
        return data
    

class SocialAccountSerializer(ModelSerializer):

    class Meta:
        model = SocialNetwork
        fields = "__all__"


class UserProfileSerializer(ModelSerializer):
    social_acc_list = SocialAccountSerializer(many=True)


    class Meta:
        model = Users
        fields = [
            'phone', 'avatar', 'full_name', 'about', 'date_joined',
            'social_acc_list', 'username']