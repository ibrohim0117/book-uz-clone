from django.urls import path, include

from .views import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('category/', CategoryListCreateAPIView.as_view(), name="category-create-list"),
    path('category/<slug:slug>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name="category_detail"),
]
