#admin.py
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Brand)
admin.site.register(Volume)
admin.site.register(Model)
(admin.site.register
 (Color))
admin.site.register(Photo)
admin.site.register(Carusel_Photo)
admin.site.register(Favorite)
admin.site.register(Basket)
admin.site.register(Order)
admin.site.register(Reviews)
admin.site.register(News)
admin.site.register(About_us)
admin.site.register(ColorPhoto)


class ProductCharacteristicInline(admin.TabularInline):
    model = Characteristic
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductCharacteristicInline]


admin.site.register(Product, ProductAdmin)

