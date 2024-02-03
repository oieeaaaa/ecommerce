from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

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

class CartView(View):
    def get(self, request):
        cart = Cart.objects.all()

        return render(request, 'website/pages/cart.html', {
            'cart': cart
        })

    def post(self, request):
        product_id = request.POST['product_id']
        quantity = request.POST['qty']
        product = get_object_or_404(Product, id=product_id)

        if int(quantity) <= 0:
            res = render(request, 'website/components/alert.html', {
                'type': 'danger',
                'message': 'Quantity must be greater than 0'
            })

            return res

        # check if cart exist
        cart = Cart.objects.filter(product=product).first()
        cartQty = int(cart.quantity) if cart is not None else 0

        if product.stock < (int(quantity) + cartQty):
            res = render(request, 'website/components/alert.html', {
                'type': 'danger',
                'message': 'Stock is not enough'
            })

            return res;

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

def cart_item_delete(request, id):
    if request.method == 'POST':
        cart = get_object_or_404(Cart, id=id)
        cart.delete()

        res = render(request, 'website/pages/cart.html', {
            'cart': Cart.objects.all()
        })
        res['HX-Trigger'] = 'cart_updated'

        return res
    else:
        return redirect('cart')


def cart_item_update(request, id):
    if request.method == 'POST':
        cart = get_object_or_404(Cart, id=id)
        product = get_object_or_404(Product, id=cart.product.id)

        qty = int(request.POST['qty'])

        if product.stock < qty:
            res = render(request, 'website/components/alert.html', {
                'type': 'danger',
                'message': 'Stock is not enough'
            })

            res['HX-Reswap'] = 'none'

            return res;

        # delete cart if qty is 0
        if qty <= 0:
            cart.delete()
        else:
            cart.quantity = qty
            cart.save()

        res = render(request, 'website/pages/cart.html', {
            'cart': Cart.objects.all()
        })

        res['HX-Trigger'] = 'cart_updated'
        return res
    else:
        return redirect('cart')

def cart_length(request):
    cart_count = Cart.objects.count()

    if cart_count <= 0:
        return HttpResponse('')

    return render(request, 'website/elements/cart-count.html', {
        'cart_count': Cart.objects.count()
    })
