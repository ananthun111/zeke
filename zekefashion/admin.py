from django.contrib import admin
from django.utils.html import format_html
from .models import *
# Register your models here.
class admin_Product(admin.ModelAdmin):
    def image_tags(self, obj):
        return format_html('<img src="{}" height="50"/>'.format(obj.image))
    image_tags.short_description = 'Image'
    list_display = ('product_id','product_name','image_tags')
    fields = ( 'product_id','product_name','image_tag','image','price','description','offer', )
    readonly_fields = ('image_tag',)
admin.site.register(Product,admin_Product)
admin.site.register(Banners)
class admin_Home_page_category(admin.ModelAdmin):
    def image_tags(self, obj):
        return format_html('<img src="{}" width="50" height="50"/>'.format(obj.Image))
    image_tags.short_description = 'Image'
    list_display = ('CategoryName','id','image_tags')
    fields = ( 'image_tag','Image','CategoryName','buttonclick', )
    readonly_fields = ('image_tag',)

admin.site.register(Home_page_category,admin_Home_page_category)
class admin_Home_page_offer(admin.ModelAdmin):
    def image_tags(self, obj):
        return format_html('<img src="{}" height="50"/>'.format(obj.image))
    image_tags.short_description = 'Image'
    list_display = ('id','image_tags')
    fields = ( 'image_tag','image','onclick', )
    readonly_fields = ('image_tag',)
admin.site.register(Home_page_offer,admin_Home_page_offer)