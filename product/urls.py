from django.urls import path, include

from .views import CategoryListCreateAPIView


urlpatterns = [
    path('category', CategoryListCreateAPIView.as_view(), name="category-create-list"),
]
