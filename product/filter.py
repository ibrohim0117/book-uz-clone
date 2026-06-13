from django_filters import rest_framework as filters
import django_filters

from product.models import Book

class ProductFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = ('slug',)

    

class BookFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    slug = django_filters.CharFilter(field_name='slug', lookup_expr='exact')
    category_slug = django_filters.CharFilter(field_name='category__slug', lookup_expr='exact')

    class Meta:
        model = Book
        fields = ['min_price', 'max_price', 'slug', 'category_slug']