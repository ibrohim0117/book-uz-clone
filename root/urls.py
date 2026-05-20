from django.contrib import admin
from django.db import router
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


from django.conf.urls.static import static
from product.views import CategoryListCreateAPIView, CategoryViewSet
from root import settings

router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/product/category', CategoryListCreateAPIView.as_view(), name="category-create-list"),
    path('api/v1/product/', include('product.urls')),
    path('api/v1/user/', include('product.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]





if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)