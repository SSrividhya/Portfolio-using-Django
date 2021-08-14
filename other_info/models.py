from django.db import models

# Create your models here.
class Info(models.Model):
    title=models.CharField(max_length=20)
    date=models.DateField()
    desc=models.TextField(max_length=5000)

    def __str__(self):
        return self.title
