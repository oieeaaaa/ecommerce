from django.shortcuts import render

from website.models import Product

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
