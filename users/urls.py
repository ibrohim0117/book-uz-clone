from django.urls import path, include
from .views import ( 
RegisterCreateAPIView, ProfileRetrieveAPIView, 
SocialAccountRetrieveUpdateDestroyAPIView,
SocialAccountListCreateAPIView
)
from rest_framework_simplejwt.views import ( 
TokenObtainPairView, TokenRefreshView, TokenBlacklistView

)




urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/', RegisterCreateAPIView.as_view(), name='register'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="refresh_token"),
    path('api/user/logout', TokenBlacklistView.as_view(), name="logout"),

    path("me/", ProfileRetrieveAPIView.as_view(), name="profile"),
    path("me/social/<int:pk>/", SocialAccountRetrieveUpdateDestroyAPIView.as_view(), name="social_update"),
    path("me/social/", SocialAccountListCreateAPIView.as_view(), name="social_create"),
 
]
