from rest_framework import serializers 
from rest_framework.serializers import ModelSerializer
from .models import Users


class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = Users
        fields = ["username", 'password', 'phone']

    def create(self, validated_data):

        user = Users.objects.create(
            username=validated_data['username'],
            password=validated_data['password'],
            phone=validated_data['phone']
        )


        return user