<<<<<<< HEAD
from django.urls import path
from .views import UserProfileView

urlpatterns = [
    path("profile/", UserProfileView.as_view()),
]
=======
from django.urls import path, include
from .views import Login, RegisterCreateAPIView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', RegisterCreateAPIView.as_view(), name='register'),
]
>>>>>>> 03f833d31d57268116088f6a4ec0b3c7a62c6afd
