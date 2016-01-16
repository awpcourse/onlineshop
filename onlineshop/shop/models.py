from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.files import File

# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=300)
    price = models.TextField()
    quantity = models.TextField()
    picture = models.ImageField(upload_to='./Pictures/',default='')
    class Meta:
        ordering = ['price']

class Wishlist(models.Model):
    id_product = models.ForeignKey(Product)
    id_user = models.ForeignKey(User)
    
class ProductComment(models.Model):
    id_product = models.ForeignKey(Product)
    id_user = models.ForeignKey(User)
    text = models.TextField()

class History(models.Model):
    id_history = models.AutoField(primary_key=True)
    id_product = models.ManyToManyField(Product)
    id_user = models.ForeignKey(User)
    date = models.DateTimeField(
        auto_now_add=True)
    
class FaultyProduct(models.Model):
    id_product = models.ForeignKey(Product)
    id_user = models.ForeignKey(User)
    return_date = models.DateTimeField()
    
class CommandLine(models.Model):
    id_user = models.ForeignKey(User)
    id_products = models.ManyToManyField(Product)
    