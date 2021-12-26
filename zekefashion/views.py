from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    banners = Banners.objects.all()
    return render(request, 'index.html',{'banners':banners})
def about(request):
    return render(request, 'about.html')
def shop(request):
    return render(request, 'shop.html')
def shopdetail(request):
    return render(request, 'shop-detail.html')
def cart(request):
    return render(request, 'cart.html')

def products(request):
    productss = Product.objects.all()
    return render(request, 'products.html', {'productss':productss})