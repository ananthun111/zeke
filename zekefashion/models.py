from django.db import models

# Create your models here.
class Product (models.Model):
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.CharField(max_length=5000, null=True, blank=True)

class Banners (models.Model):
    image = models.CharField(max_length=5000, null=True, blank=True)
    firstline = models.CharField(default='Welcome To',max_length=50)
    secandline = models.CharField(default='Freshshop',max_length=50)
    therdline = models.CharField(default='See how your users experience your website in realtime or view',max_length=200)
    forthline = models.CharField(default='trends to see any changes in performance over time.',max_length=200)
    buttontext = models.CharField(default='Shop New',max_length=50)
    buttonclick = models.URLField(default='http://127.0.0.1:8000/', max_length=200)