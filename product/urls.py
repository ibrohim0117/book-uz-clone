from django.urls import path, include

from .views import (
    CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView,
    BookRetrieveUpdateDestroyAPIView, BookListCreateAPIView, AuthorCreateApiView
)


urlpatterns = [
    path('category/', CategoryListCreateAPIView.as_view(), name="category-create-list"),
    path('category/<slug:slug>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name="category_detail"),

    path('book/<slug:slug>/', BookRetrieveUpdateDestroyAPIView.as_view(), name="book_detail"),
    path('book/', BookListCreateAPIView.as_view(), name="book-create-list"),
    
    path('author-create/', AuthorCreateApiView.as_view(), name="author-create"),
]
