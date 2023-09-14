from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Product, Image, Category

class ProductAdmin(ModelAdmin):
    pass

admin.site.register(Product,ProductAdmin)

class ImageAdmin(ModelAdmin):
    pass

admin.site.register(Image,ImageAdmin)

class CategoryAdmin(ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
