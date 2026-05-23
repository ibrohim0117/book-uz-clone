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