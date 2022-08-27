from unicodedata import category
from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=50, null=True)

class Prodcut(models.Model):
    name = models.TextField(null=True)
    price = models.FloatField()
    # seller = models.ForeignKey(null=True, on_delete=models.CASCADE)
    img = models.FileField()
    createdAt = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

