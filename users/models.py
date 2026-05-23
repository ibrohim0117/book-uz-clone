from django.db import models
from django.contrib.auth.models import AbstractUser


class SocialNetwork(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Users(AbstractUser):
    class RoleChoices(models.TextChoices):
        ADMIN = "admin", "Admin"
        CLIENT = "client", "Client"

    phone = models.CharField(max_length=23, unique=True, blank=True, null=True)
    avatar = models.ImageField(upload_to="users/", blank=True, null=True)
    role = models.CharField(max_length=15, choices=RoleChoices.choices, default=RoleChoices.CLIENT)
    about = models.TextField(blank=True, null=True)
    social_network = models.ManyToManyField(SocialNetwork, related_name='social_network', null=True, blank=True)
    



