from django.db import models
from django.contrib.auth.models import AbstractUser
from product.models import BaseCreateModel

class Users(AbstractUser, BaseCreateModel):
    avatar = models.ImageField(upload_to="user_avatar/", blank=True, null=True)
    phone = models.CharField(max_length=20)
    
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