from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from root import settings

from rest_framework.routers import DefaultRouter  
from rest_framework.authtoken import views as drf_views 
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from product import views as product_views
from product.views import CategoryListCreateAPIView

router = DefaultRouter()  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/product/category', CategoryListCreateAPIView.as_view(), name="category-create-list"),
    path('api/v1/product/', include('product.urls')),
    
    path('api/v1/user/', include('users.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    #basic auto uchu
    path('api-login/', drf_views.obtain_auth_token),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
