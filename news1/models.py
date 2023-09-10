from django.db import models
import uuid
from django.contrib.auth.models import User
from django.conf import settings
import datetime

# Create your models here.
class Category1(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=500)
    tagline = models.TextField(max_length=200)

    class Meta:
        verbose_name_plural = "Category1"
    def __str__(self):
        return self.name
    
class Continent1(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Continent1"
    def __str__(self):
        return self.name
    
class Region1(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Region1"
    def __str__(self):
        return self.name


class News1(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    headline = models.CharField(max_length=500)
    content = models.TextField()
    image = models.ImageField(upload_to="images")
    category = models.ForeignKey(Category1, on_delete=models.CASCADE)
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photographer = models.CharField(max_length=100)
    continent = models.ForeignKey(Continent1, on_delete=models.CASCADE)
    region = models.ForeignKey(Region1, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "News1"
        ordering = ['-created']

    def __str__(self):
        return self.headline