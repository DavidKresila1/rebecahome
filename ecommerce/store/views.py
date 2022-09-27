from itertools import product
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from cart.cart import Cart
from django.views.generic import ListView

from .models import Product


class ProductList(ListView):
    model = Product


def productdetail(request,id):
    product = Product.objects.get(id)
    return render(request, 'store/product_list.html', {'product': product})

def homePage(request):
    products = None
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(category=category_id)
    else:
        products = Product.objects.filter(category=1)
    context = {'products': products, 'categories': categories}
    return render(request, 'store/home.html', context)


def login(request):
    return render(request, 'store/login.html')

def contact(request):
    return render(request, "store/contact.html")





def test(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, 'store/test.html', context)

def add_to_card(request, product_id, quantity):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.price, quantity)

def remove_from_cart(requset, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(requset)
    cart.remove(product)

def get_cart(request):
    return render(request, "store/cart.html", {"cart": Cart(request)})














