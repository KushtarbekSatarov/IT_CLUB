from django_filters.rest_framework import FilterSet
from .models import Product, Brand, Model, Volume


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'memory': ['gt', 'lt'],
            'price': ['gt', 'lt']

        }


