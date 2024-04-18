from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.BooleanField()
    email = models.EmailField(unique=True, blank=False)
    image = models.ImageField()
    file =  models.FileField()
    address= models.TextField(null=True , blank=True)

                                 

class product(models.Model):
    pass