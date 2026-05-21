from django.db import models
from django.contrib.auth.models import AbstractUser
from product.models import BaseCreateModel

#user model
class Users(AbstractUser):
    class UserTypes(models.TextChoices):
        Admin = 'Admin', 'Admin'
        OPERATOR = 'Operator', 'Operator'
        CLENT = 'Clent', 'Mijoz'
        
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    user_type = models.CharField(max_length=500, choices=UserTypes.choices, default=UserTypes.CLENT)
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.username
    
    @property
    def full_name(self):
        return f"{self.first_name} - {self.last_name}"