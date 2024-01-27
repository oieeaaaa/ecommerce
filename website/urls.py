from django.urls import path

# import all from .views
from .views import CartView, cart_item_delete, cart_item_update, index
from .views import product_detail

urlpatterns = [
    path('', index, name='home'),
    path('products/<int:id>', product_detail, name='product_detail'),
    path('cart', CartView.as_view(), name='cart'),
    path('cart/<int:id>/delete', cart_item_delete, name='cart_item_delete'),
    path('cart/<int:id>/update', cart_item_update, name='cart_item_update'),
]
