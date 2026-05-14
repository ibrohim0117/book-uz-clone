from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from root import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/product/', include('product.urls')),
    path('api/v1/user/', include('users.urls'))
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
