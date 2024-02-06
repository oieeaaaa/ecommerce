from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.db.models import Q

from website.models import Category, Product, Cart

# Create your views here.


# TODO:
# - Category filter and home filter cancels each other
def index(request):
    categories = Category.objects.all()[:10]
    filters = request.session.get('filters', {})
    products = []

    if filters:
        filtersQ = Q()
        for key in filters:
            filtersQ |= Q(categories__name=key)

        products = Product.objects.filter(filtersQ)[:10]
    else:
        products = Product.objects.all()[:10]

    return render(request, 'website/pages/home.html', {
        'products': products,
        'categories': categories,
        'filters': filters
    })


class Filter(View):
    def post(self, request):
        form = request.POST
        sessionFilters = dict()

        for key in form:
            if key.find('category') != -1:
                try:
                    key = key.split('.')[1]
                    sessionFilters[key] = True
                except Category.DoesNotExist:
                    return HttpResponse('Invalid category name')

        # set filters to session
        request.session['filters'] = sessionFilters

        res = HttpResponse()
        res['HX-Trigger'] = 'filters_changed'

        return res


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

            return res

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

            return res

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


class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        filters = request.session.get('filters', {})

        return render(request, 'website/components/filters.html', {
            'categories': categories,
            'filters': filters
        })
