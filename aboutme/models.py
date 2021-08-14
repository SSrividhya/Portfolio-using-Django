from django.db import models

# Create your models here.
class Aboutme(models.Model):
    title=models.CharField(max_length=50)
    desc=models.CharField(max_length=100)
    image=models.ImageField(upload_to='aboutme/images')
    url=models.URLField(blank=True)
