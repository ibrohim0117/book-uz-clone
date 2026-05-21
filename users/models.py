from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    class RoleChoices(models.TextChoices):
        ADMIN = "admin", "Admin"
        CLIENT = "client", "Client"

    first_name = models.CharField(max_length=220)
    last_name = models.CharField(max_length=220)
    phone = models.CharField(max_length=23, unique=True)
    avatar = models.ImageField(upload_to="users/", blank=True, null=True)
    role = models.CharField(max_length="15", choices=RoleChoices.choices, default=RoleChoices.CLIENT)
    about = models.TextField()
    theme_dark = models.BooleanField(default=False)

