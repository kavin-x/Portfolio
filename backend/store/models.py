from distutils.command.upload import upload
from importlib.util import set_loader
from operator import mod
from tabnanny import verbose
from turtle import ondrag
from django.db import models

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=255,db_index=True)
    slug = models.SlugField(max_length=255,db_index=True)

    class Meta:
        verbose_name_plural='categories'

    def __str__(self) :
        return self.name


class Product(models.Model):
    category= models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    Category= models.ForeignKey(User,related_name='product_creator',on_delete=models.CASCADE)
    author= models.CharField(max_length=255,default='admin')
    title= models.CharField(max_length=255)
    description= models.CharField(blank=True)
    image= models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255,db_index=True)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    in_stock = models.BooleanField(default=True)
    in_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='Products'
        ordering = ('-created',)

    def __str__(self) :
        return self.title    