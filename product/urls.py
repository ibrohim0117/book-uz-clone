from django.urls import path

from .views import (
    CategoryListAPIView, CategoryRetrieveUpdateDestroyAPIView,
    BookRetrieveUpdateDestroyAPIView, CategoryCreateAPIView,
    BookListAPIView, BookCreateAPIView
)


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name="category-list"),
    path('categories/create/', CategoryCreateAPIView.as_view(), name="category-create"),
    path('categories/<slug:slug>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name="category-detail"),

    path('book/<slug:slug>/', BookRetrieveUpdateDestroyAPIView.as_view(), name="book_detail"),
    path('book/', BookListAPIView.as_view(), name="book_list"),
    path('book-create/', BookCreateAPIView.as_view(), name="book-create"),
]
