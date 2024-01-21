from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.URLField(max_length=2083)
    created_at = models.DateTimeField(auto_now_add=True)
