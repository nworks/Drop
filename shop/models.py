from __future__ import unicode_literals
from PIL import Image
from django.db import models

# Create your models here.
class Product(models.Model):
	profile_image = models.ImageField(upload_to="static/img/Products", blank=True, null=True)
	product_name = models.CharField(max_length=200)
	product_type = models.CharField(max_length=200)
	product_price = models.DecimalField( max_digits=19, decimal_places=2)
	description = models.TextField()
	stock = models.DecimalField(max_digits=19, decimal_places=0)
	vote =  models.DecimalField(max_digits=1, decimal_places=0)
	vacio1 = models.CharField(max_length=200)
	vacio2 = models.CharField(max_length=200)
	vacio3 = models.CharField(max_length=200)