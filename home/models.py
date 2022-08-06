from django.db import models
from django.forms import ImageField

# Create your models here.

class GalleryModel(models.Model):
    Image = models.ImageField(upload_to='images/', null=True,blank=True)
    Name = models.CharField(max_length=25)
    ModelName = models.CharField(max_length=25)
    Price = models.IntegerField()
    Description = models.CharField(max_length=225)

    def __str__ (self):
        return self.Name