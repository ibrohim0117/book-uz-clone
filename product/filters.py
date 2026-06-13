import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    slug = django_filters.CharFilter(field_name="slug", lookup_expr='icontains')
    
    class Meta:
        model = Book
        fields = ['min_price', 'max_price', 'slug']