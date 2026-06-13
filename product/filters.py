from django_filters import rest_framework as filters
from .models import Book

class FilterMaxMinValue(filters.FilterSet):

    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    min_price = filters.NumberFilter(field_name='price', lookup_expr="gte")
    max_price = filters.NumberFilter(field_name='price', lookup_expr="lte")

    class Meta:
        model = Book
        fields = ['name', 'min_price', 'max_price']

    #tips __gte (Greater than or equal to - katta yoki teng) va __lte (Less than or equal to - kichik yoki teng)
