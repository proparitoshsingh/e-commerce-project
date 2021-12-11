from django.db import models
from django.db.models.fields import AutoField, CharField
from accounts.models import User
from products.models import Product

class Order(models.Model):

    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)