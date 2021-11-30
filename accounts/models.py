from django.db import models
from jsonfield import JSONField

class Cart:
    items = {} # "productID" : Product object

    def add_to_cart(self, pid, obj):
        self.items[pid] = obj

    def del_from_cart(self, pid):
        del self.items[pid]

class User(models.Model):
    name = models.CharField(max_length=128, blank=True)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=128, blank=False, null=False)
    confirmed = models.BooleanField(default=False)
    cart = Cart()
    cartJSON = JSONField(Cart.items, default=None)

    def __str__(self):
        return self.email