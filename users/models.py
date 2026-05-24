from django.db import models
from django.contrib.auth.models import AbstractUser
from product.models import BaseCreateModel

class Users(AbstractUser, BaseCreateModel):
    avatar = models.ImageField(upload_to="user_avatar/", blank=True, null=True)
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.username