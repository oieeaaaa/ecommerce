from django.urls import path

# import all from .views
from .views import CartView, CategoryView, HomeFilter, cart_length, cart_item_delete, cart_item_update, index
from .views import product_detail

urlpatterns = [
    path('', index, name='home'),
    path('filter', HomeFilter.as_view(), name='filter'),
    path('categories', CategoryView.as_view(), name='categories'),
    path('products/<int:id>', product_detail, name='product_detail'),
    path('cart', CartView.as_view(), name='cart'),
    path('cart/<int:id>/delete', cart_item_delete, name='cart_item_delete'),
    path('cart/<int:id>/update', cart_item_update, name='cart_item_update'),
    path('cart/length', cart_length, name='cart_count'),
]
