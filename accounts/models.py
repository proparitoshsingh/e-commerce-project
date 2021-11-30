from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=128, blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=128, blank=False, null=False)

    def __str__(self):
        return self.email