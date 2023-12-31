from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)
    class Meta:        
        verbose_name_plural = "Category"
    def __str__(self):
            return self.category

class SliderNews(models.Model):
    image = models.ImageField(upload_to="my-images")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    headline = models.CharField(max_length=500) 
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)


    class Meta:        
        verbose_name_plural = "SliderNews"
    def __str__(self):
            return self.headline
    
class NewsLetter(models.Model):
    email = models.EmailField()
    class Meta:
        verbose_name_plural = "NewsLetter"
    def __str__(self):
        return self.email
class Enquiries(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    subject = models.CharField(max_length=100)
    information = models.TextField()

    class Meta:
         verbose_name_plural = "Enquiries"
    def __str__(self):
         return self.name
    
class UserComments(models.Model):
     user_image = models.ImageField(upload_to="user_images")
     user_name = models.CharField(max_length=50)
     comment_date = models.DateTimeField(default=timezone.now)
     comment = models.TextField(max_length=500)

    


        