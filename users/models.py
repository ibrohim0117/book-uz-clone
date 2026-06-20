from uuid import uuid4
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken


class Users(AbstractUser):
    class RoleChoices(models.TextChoices):
        ADMIN = "admin", "Admin"
        CLIENT = "client", "Client"

    phone = models.CharField(max_length=23, unique=True, blank=True, null=True)
    avatar = models.ImageField(upload_to="users/", blank=True, null=True)
    role = models.CharField(max_length=15, choices=RoleChoices.choices, default=RoleChoices.CLIENT)
    about = models.TextField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

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

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class SocialNetwork(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField(max_length=500, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Users o'rniga settings.AUTH_USER_MODEL qo'yildi:
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='social_acc_list')

    def __str__(self):
        return self.title


class Cart(models.Model):
    # Users o'rniga settings.AUTH_USER_MODEL qo'yildi:
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_cart")
    book = models.ForeignKey('product.Book', on_delete=models.CASCADE, related_name="cart_item", null=True)
    count = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # self.product.name o'rniga self.book.title (yoki name) deb to'g'rilandi:
        return f"{self.user.username} - {self.book}"