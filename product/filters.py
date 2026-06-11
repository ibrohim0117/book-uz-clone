import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    # Narx bo'yicha filter: ?min_price=10&max_price=50
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    # Slug bo'yicha category filter: ?category_slug=fantasy
    category_slug = django_filters.CharFilter(field_name='category__slug', lookup_expr='exact')

    class Meta:
        model = Book
        fields = ['min_price', 'max_price', 'category_slug']
