from django.db import models

# Create your models here.
class gallery_images(models.Model):
    image = models.ImageField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    text=models.CharField(max_length=50)
    ashok=models.CharField(max_length=50)
