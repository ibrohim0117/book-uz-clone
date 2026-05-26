from django.urls import path

from .views import (
    CategoryListAPIView, CategoryCreateAPIView, CategoryRetrieveUpdateDestroyAPIView,
    BookListAPIView, BookCreateAPIView, BookRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name="category-list"),
    path('categories/create/', CategoryCreateAPIView.as_view(), name="category-create"),
    path('categories/<slug:slug>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name="category-detail"),

    path('books/', BookListAPIView.as_view(), name="book-list"),
    path('books/create/', BookCreateAPIView.as_view(), name="book-create"),
    path('books/<slug:slug>/', BookRetrieveUpdateDestroyAPIView.as_view(), name="book-detail"),
]
