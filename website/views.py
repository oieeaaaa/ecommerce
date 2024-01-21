from django.shortcuts import get_object_or_404, redirect, render

from website.models import Product, Cart

# Create your views here.


def index(request):
    products = Product.objects.all()

    return render(request, 'pages/home.html', {
        'products': products,
    })


def product_detail(request, id):
    product = Product.objects.get(id=id)

    return render(request, 'pages/product-detail.html', {
        'product': product,
    })


# TODO:
# x check if product exist
# x check if product stock is enough
# x handle create a cart
# x handle same cart item add
# x handle update product stock
# - handle cart quantity update
# - handle cart item delete
def cart(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        quantity = request.POST['qty']
        product = get_object_or_404(Product, id=product_id)

        if product.stock < int(quantity):
            return redirect('cart')

        product.stock -= int(quantity)
        product.save()

        # check if cart exist
        cart = Cart.objects.filter(product=product).first()

        if cart:
            cart.quantity += int(quantity)
            cart.save()
            return redirect('cart')
        else:
            # create a cart
            cart = Cart.objects.create(product=product, quantity=quantity)
            cart.save()

        # redirect to cart page
        return redirect('cart')

    cart = Cart.objects.all()
    return render(request, 'pages/cart.html', {
        'cart': cart
    })
