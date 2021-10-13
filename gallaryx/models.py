from django.db import models

# Create your models here.

class Location(models.Model):
   name = models.CharField(max_length=30)

class Category (models.Model):
    list = models.CharField(max_length =30)

class photos (models.Model):
    photo = models.ImageField(upload_to= 'photo/')
    description =models.TextField(max_length=30)
    location= models.ForeignKey(Location,on_delete=models.CASCADE)
    Category = models.TextField(max_length=30)

    