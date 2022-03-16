from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.forms import model_to_dict

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = ('categories')
    def __str__(self):
        return self.name 

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Products'
    


