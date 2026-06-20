from django_filters import rest_framework as filters
from .models import Book, Category

class FilterMaxMinValue(filters.FilterSet):

    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    min_price = filters.NumberFilter(field_name='price', lookup_expr="gte")
    max_price = filters.NumberFilter(field_name='price', lookup_expr="lte")
    category = filters.NumberFilter(field_name='category_id')
    category_name = filters.CharFilter(field_name='category__name', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['name', 'min_price', 'max_price', 'category', 'category_name']



class CategoryFilter(filters.FilterSet):
    """category-list uchun parent id bo'yicha filter (TODO item 4)"""

    parent = filters.NumberFilter(field_name='parent_id')

    class Meta:
        model = Category
        fields = ['name', 'parent']

