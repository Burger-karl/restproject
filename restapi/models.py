from django.db import models

# Create your models here.

class Info(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

