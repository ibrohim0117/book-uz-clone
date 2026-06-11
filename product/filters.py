from .models import Book
from django_filters import rest_framework as filters

class FilterMaxMinValue(filters.FilterSet):
    
    min_price = filters.NumberFilter(field_name='price', lookup_expr="gte")
    max_price = filters.NumberFilter(field_name='price', lookup_expr="lte")

    class Meta:
        model = Book
        fields = ['min_price', 'max_price']

    #tips __gte (Greater than or equal to - katta yoki teng) va __lte (Less than or equal to - kichik yoki teng)
