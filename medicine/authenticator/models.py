from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Login(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    manufacturer_name = models.TextField(max_length=80, default="Not Specified")


class Product(models.Model):
    manufacturer = models.CharField(max_length=80, default="Not Specified")
    product_name = models.CharField(max_length=80)
    price = models.CharField(max_length=80)
    expiry = models.CharField(max_length=80)
    packing = models.CharField(max_length=80)


class BatchNumber(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    batch_no = models.CharField(max_length=80)
