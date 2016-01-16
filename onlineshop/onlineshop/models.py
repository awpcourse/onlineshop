from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.files import File

class Product(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=300)
    price = models.TextField()
    quantity = models.TextField()
    picture = models.ImageField(upload_to='./Pictures/',default='')
    class Meta:
        ordering = ['price']

class WishList(models.Model):
    id_product 
    