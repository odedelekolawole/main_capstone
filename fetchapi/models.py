from django.db import models

# Create your models here.
class News2(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    description = models.TextField()
    url = models.URLField()
    image = models.URLField()
    published = models.DateTimeField()
    content = models.TextField()

    class Meta:
        verbose_name_plural = "News2"        
        
    def __str__(self):
            return self.title
        

