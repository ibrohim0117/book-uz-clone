from django.urls import path, include

from .views import CategoryListCreateAPIView, get_category_detail


urlpatterns = [
    path('category/', CategoryListCreateAPIView.as_view(), name="category-create-list"),
    path('category/<slug:slug>/', get_category_detail, name="category_detail"),
]
