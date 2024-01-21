from django.urls import path
from .views import cart, index, product_detail

urlpatterns = [
    path('', index, name='home'),
    path('products/<int:id>', product_detail, name='product_detail'),
    path('cart', cart, name='cart'),
]
