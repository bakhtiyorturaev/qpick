
from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    search_fields = ('name',)
    list_filter = ('category',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
