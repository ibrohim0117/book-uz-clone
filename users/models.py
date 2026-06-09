from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password


class Users(AbstractUser):
    class RoleChoices(models.TextChoices):
        ADMIN = "admin", "Admin"
        CLIENT = "client", "Client"

    phone = models.CharField(max_length=23, unique=True, blank=True, null=True)
    avatar = models.ImageField(upload_to="users/", blank=True, null=True)
    role = models.CharField(max_length=15, choices=RoleChoices.choices, default=RoleChoices.CLIENT)
    about = models.TextField(blank=True, null=True)

    def token(self):
        refresh = RefreshToken.for_user(self)
        access = str(refresh.access_token)

        data = {
            'access': access,
            'refresh': str(refresh)
        }

        return data

    def __str__(self):
        return self.username
    

class SocialNetwork(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='social_acc_list')

    def __str__(self):
        return self.title
