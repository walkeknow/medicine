from django.contrib import admin

from .models import Login
from .models import BatchNumber
from .models import Product

# Register your models here.
admin.site.register(Login)
admin.site.register(BatchNumber)
admin.site.register(Product)