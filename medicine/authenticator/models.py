from django.db import models


# Create your models here.
class Login(models.Model):
    manufacturer_name = models.TextField(max_length=40)
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=20)


class Manufacturer(models.Model):
    manufacturer = models.ForeignKey('Login', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=20)


class Product(models.Model):
    product = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    brand = models.CharField(max_length=40)
    packing = models.CharField(max_length=20)
    batch_no = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    expiry = models.CharField(max_length=20)
