from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': "Bu email manzili allaqachon ro'yxatdan o'tgan.",
        },
        verbose_name="Email manzili"
    )
    
    phone_number = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        verbose_name="Telefon raqami"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Ro'yxatdan o'tgan sana"
    )

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"
        db_table = 'users_user' 

    def __str__(self):
        return self.username



class Users(AbstractUser):
    class RoleChoices(models.TextChoices):
        ADMIN = "admin", "Admin"
        CLIENT = "client", "Client"

    phone = models.CharField(max_length=23, unique=True, blank=True, null=True)
    avatar = models.ImageField(upload_to="users/", blank=True, null=True)
    role = models.CharField(max_length=15, choices=RoleChoices.choices, default=RoleChoices.CLIENT)
    about = models.TextField(blank=True, null=True)

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


