from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from website.models import Product, Cart

# Create your views here.


def index(request):
    products = Product.objects.all()

    return render(request, 'website/pages/home.html', {
        'products': products,
    })


def product_detail(request, id):
    product = Product.objects.get(id=id)

    return render(request, 'website/pages/product-detail.html', {
        'product': product,
    })

# TODO:
# x check if product exist
# x check if product stock is enough
# x handle create a cart
# x handle same cart item add
# x handle update product stock
# x handle cart quantity update
# x handle cart item delete
# x handle redirect after adding to cart
def cart(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        quantity = request.POST['qty']
        product = get_object_or_404(Product, id=product_id)

        # check if cart exist
        cart = Cart.objects.filter(product=product).first()
        cartQty = int(cart.quantity) if cart is not None else 0

        if product.stock < (int(quantity) + cartQty):
            return render(request, 'website/pages/product-detail.html', {
                'product': product,
                'errors': {
                    'qty': 'Stock is not enough'
                },
            })

        if cart:
            cart.quantity += int(quantity)
            cart.save()
        else:
            # create a cart
            cart = Cart.objects.create(product=product, quantity=quantity)
            cart.save()

        # redirect to cart page
        # add custom header to response
        response = HttpResponse()

        response['HX-Reswap'] = 'none'
        response['HX-Location'] = '/cart'

        return response
    else:
        return render(request, 'website/pages/cart.html', {
            'cart': Cart.objects.all()
        })


def cart_item_delete(request, id):
    if request.method == 'POST':
        cart = get_object_or_404(Cart, id=id)
        cart.delete()

        return render(request, 'website/pages/cart.html', {
            'cart': Cart.objects.all()
        })
    else:
        return redirect('cart')


def cart_item_update(request, id):
    if request.method == 'POST':
        cart = get_object_or_404(Cart, id=id)
        product = get_object_or_404(Product, id=cart.product.id)

        qty = int(request.POST['qty'])

        if product.stock < qty:
            return redirect('cart')

        cart.quantity = qty
        cart.save()

        return render(request, 'website/pages/cart.html', {
            'cart': Cart.objects.all()
        })
    else:
        return redirect('cart')
