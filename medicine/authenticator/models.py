from django.db import models


# Create your models here.
class Login(models.Model):
    manufacturer_name = models.TextField(max_length=80)
    password = models.CharField(max_length=80)
    email = models.CharField(max_length=80)


class Manufacturer(models.Model):
    manufacturer = models.ForeignKey('Login', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=80)


class Product(models.Model):
    product = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    packing = models.CharField(max_length=80)
    batch_no = models.CharField(max_length=80)
    price = models.CharField(max_length=80)
    expiry = models.CharField(max_length=80)
