from django.urls import path
from .views import CategoryListCreateAPIView, CategoryDetailUpdateDeleteAPIView

urlpatterns = [
    path('', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('api/v1/product/category/<slug:slug>', CategoryDetailUpdateDeleteAPIView.as_view(), name='category-detail-update-delete'),
]