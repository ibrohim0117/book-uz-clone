from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	"""Custom User model for the project.

	Currently inherits from `AbstractUser` to preserve Django's default
	authentication behavior while allowing future customization.
	"""
	pass
