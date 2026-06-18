from django.urls import path, include
from .views import ( 
    RegisterCreateAPIView, ProfileRetrieveAPIView,
    SocialNetworkListCreateAPIView, SocialNetworkRetrieveUpdateDestroyAPIView
)
from rest_framework_simplejwt.views import ( 
    TokenObtainPairView, TokenRefreshView, TokenBlacklistView,
)




urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/', RegisterCreateAPIView.as_view(), name='register'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('api/user/logout', TokenBlacklistView.as_view(), name='logout'),

    path('profile/', ProfileRetrieveAPIView.as_view(), name='profile'),

    path('social_network/', SocialNetworkListCreateAPIView.as_view(), name='social_network-create'),
    path('social_network/<int:pk>/', SocialNetworkRetrieveUpdateDestroyAPIView.as_view(), name='social_network'),
]