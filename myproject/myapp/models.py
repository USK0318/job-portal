from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    user=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username