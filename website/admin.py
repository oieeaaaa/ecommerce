from django.contrib import admin

# Register your models here.

from .models import Cart, Product, Category

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Category)
