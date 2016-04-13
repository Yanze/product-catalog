from django.db import models
# from django import forms
from datetime import datetime
from django.core.urlresolvers import reverse

# Create your models here.
class Product(models.Model):
        brand = models.CharField(max_length=20, default="")
        name = models.CharField(max_length=100, default="")
        price = models.IntegerField(default=0)
        description = models.TextField(default="")
        added = models.DateTimeField(default=datetime.now, blank=True)

        def __str__(self):
            return 'self.brand: {}, self.name: {}, self.price: {}, self.description: {}, self.added: {}'.format(self.brand, self.name, self.price,self.description,self.added)
