from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('shop-detail/', views.shopdetail, name='shop-detail'),
    path('cart/', views.cart, name='cart'),
    path('products/', views.products, name='products'),

]