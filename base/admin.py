from django.contrib import admin
from .models import Category, Prodcut
# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category,CategoryAdmin)


class ProdcutAdmin(admin.ModelAdmin):
    list_display = ['name', 'price',]

admin.site.register(Prodcut,ProdcutAdmin)
