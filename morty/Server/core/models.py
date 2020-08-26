from django.db import models

# Create your models here.

class ImageData(models.Model):
    name = models.CharField(max_length=50)
    filename = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Image Data'
