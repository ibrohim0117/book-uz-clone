from django.db import models
from django.contrib.auth.models import AbstractUser



class SocialNetwork(models.Model):
    url = models.CharField(max_length=500)



class Users(AbstractUser):
    class RoleChoices(models.TextChoices):
        ADMIN = "admin", "Admin"
        CLIENT = "client", "Client"


    phone = models.CharField(max_length=23, unique=True)
    avatar = models.ImageField(upload_to="users/", blank=True, null=True)
    role = models.CharField(max_length="15", choices=RoleChoices.choices, default=RoleChoices.CLIENT)
    about = models.TextField(blank=True, null=True)
    theme_dark = models.BooleanField(default=False)
    social_network = models.ForeignKey(SocialNetwork, on_delete=models.CASCADE, related_name='social_network')
    



