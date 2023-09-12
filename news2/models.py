from django.db import models

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
    date = models.DateTimeField(auto_now_add=True)

    class Meta:        
        verbose_name_plural = "SliderNews"
    def __str__(self):
            return self.headline
        