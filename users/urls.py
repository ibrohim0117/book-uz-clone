from django.urls import path
# from .views import UserProfileView
from .views import Login, RegisterCreateAPIView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', RegisterCreateAPIView.as_view(), name='register'),
]