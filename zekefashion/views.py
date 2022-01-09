from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    banners = Banners.objects.all()
    product = Product.objects.all()
    categorys = Home_page_category.objects.all()
    offers = Home_page_offer.objects.all() 
    return render(request, 'index.html',{'banners':banners ,'categorys':categorys,'offers':offers,'products':product})
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