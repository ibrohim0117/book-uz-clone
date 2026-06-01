from django.urls import path, include
from .views import RegisterCreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/', RegisterCreateAPIView.as_view(), name='register'),
]
