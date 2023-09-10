from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email) # The normalize_email helps us to turn a string to a valid email
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff been True")        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")
        
        return self.create_user(email=email, password=password, **extra_fields)

class User(AbstractUser):
    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username



