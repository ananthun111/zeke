from django.db import models

# Create your models here.
class Product (models.Model):
    product_id = models.CharField(max_length=5000, null=True)
    product_name = models.CharField(max_length=200,default="Lorem ipsum dolor sit amet")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(default="Lorem ipsum dolor sit amet")
    offer = models.CharField(max_length=10)
    image = models.CharField(max_length=5000, null=True, blank=True)
    class Meta:
        db_table = 'product' # table name in data base
        verbose_name = "Product"
    def __str__(self):
        return self.product_id
    def image_tag(self):
        from django.utils.html import format_html
        return format_html('<img src="{}" height="200"/>'.format(self.image))
    image_tag.short_description = 'Images'  

class Banners (models.Model):
    image = models.CharField(max_length=5000, null=True, blank=True)
    firstline = models.CharField(default='Welcome To',max_length=50)
    secandline = models.CharField(default='Freshshop',max_length=50)
    therdline = models.CharField(default='See how your users experience your website in realtime or view',max_length=200)
    forthline = models.CharField(default='trends to see any changes in performance over time.',max_length=200)
    buttontext = models.CharField(default='Shop New',max_length=50)
    buttonclick = models.URLField(default='http://127.0.0.1:8000/', max_length=200)

class Home_page_category (models.Model):
    Image = models.CharField(max_length=5000, null=True, blank=True)
    CategoryName = models.CharField(default='Category Name',max_length=50)
    buttonclick = models.URLField(default='http://127.0.0.1:8000/', max_length=200)
    class Meta:
        db_table = 'category' # table name in data base
        verbose_name = "Category"
    def __str__(self):
        return self.CategoryName # show str for ech object
    def image_tag(self):
        from django.utils.html import format_html
        return format_html('<img src="{}" width="200" height="200"/>'.format(self.Image))
    image_tag.short_description = 'Images'  

class Home_page_offer (models.Model):
    image = models.CharField(max_length=5000, null=True, blank=True)
    onclick = models.URLField(default='http://127.0.0.1:8000/', max_length=200)
    class Meta:
        db_table ='Homepageoffer'
        verbose_name = "Home page offer"
    def _str_(self):
        return self.id
    def image_tag(self):
        from django.utils.html import format_html
        return format_html('<img src="{}" height="200"/>'.format(self.image))
    image_tag.short_description = 'Images'