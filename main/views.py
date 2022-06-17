from django.http import Http404
from django.shortcuts import render

from main.models import Product


def products_list(request):
    products = Product.objects.all()
    #SELECT * FROM product;
    #products/?price_from=50000&price_to=110000
    #request.GET #{'price_from': 50000, 'price_to': 110000}
    price_from = request.GET.get('price_from')
    price_to = request.GET.get('price_to')
    if price_from and price_to:
        # products_filtered = products.filter(price__gt=price_from, price__lt=price_to)
        products_filtered = products.filter(price__range=[price_from, price_to])
        return render(request, 'main/products.html', {'products': products_filtered})
    return render(request, 'main/products.html', {'products': products})


def product_details(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        return render(request, 'main/details.html', {'product': product})
    except Product.DoesNotExist:
        raise Http404
