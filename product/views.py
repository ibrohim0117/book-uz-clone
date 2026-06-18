from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from .models import Category, Book, Author
from .serializers import (
    CategorySerializer, CategoryDetailSerializer,
    CategoryUpdateSerializer, BookSerializer, BookUpdateSerializer,
    BookCreateSerializer, AuthorCreateSerializer
)
from .permissions import IsAdminRoleUser
from .pagination import BookPagination
from .filters import BookFilter




@extend_schema(tags=['category'])
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsAdminRoleUser()]
        return [AllowAny()]


@extend_schema(tags=['category/slug'])
class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminUser(), IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategoryDetailSerializer
        elif self.request.method == "PUT":
            return CategoryUpdateSerializer
        return self.serializer_class




@extend_schema(tags=['book'])
class BookListCreateAPIView(ListCreateAPIView):
    """
    Kitoblar ro'yxati va yaratish.

    Query parametrlar:
    - page         : sahifa raqami (default: 1)
    - limit        : sahifadagi elementlar soni (default: 10)
    - min_price    : minimal narx filtri
    - max_price    : maksimal narx filtri
    - category_slug: kategoriya slug bo'yicha filter
    - search       : kitob nomi yoki tavsifi bo'yicha qidiruv (katta-kichik harf farqlamaydi)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Pagination
    pagination_class = BookPagination

    # Filter + Search backends
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BookFilter                    # min_price, max_price, category_slug
    search_fields = ['name', 'about']               # ?search=...

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminUser(), IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookCreateSerializer
        return BookSerializer

    def perform_create(self, serializer):
        return serializer.save(add_user=self.request.user)


@extend_schema(tags=['book/slug'])
class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminUser(), IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookSerializer
        elif self.request.method == "PUT":
            return BookUpdateSerializer
        return self.serializer_class




@extend_schema(tags=["Author"])
class AuthorCreateApiView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorCreateSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated(), IsAdminUser()]

    def perform_create(self, serializer):
        return serializer.save(add_user=self.request.user)
