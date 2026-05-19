from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from product.views import CategoryListCreateAPIView
from root import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/product/category', CategoryListCreateAPIView.as_view(), name="category-create-list"),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)