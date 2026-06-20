from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from product.permissions import (IsAdminRoleUser, IsOwner)


from rest_framework.generics import (
    CreateAPIView, RetrieveUpdateDestroyAPIView,
    RetrieveAPIView, RetrieveUpdateAPIView,
    ListCreateAPIView
)

from .serializers import (
    UserRegisterSerializer, UserProfileSerializer,
    SocialAccountSerializer, UserCartSerializer,
    SocialAccountListSerializer
)

from .models import Users, SocialNetwork



@extend_schema(tags=['Register'])
class RegisterCreateAPIView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserRegisterSerializer

    


@extend_schema(tags=['User/Profile'])
class ProfileRetrieveAPIView(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    


@extend_schema(tags=['social_account-create'])
class SocialAccountListCreateAPIView(ListCreateAPIView):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialAccountSerializer
    permission_classes = [IsAuthenticated, ]


    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)



@extend_schema(request=SocialAccountSerializer, tags=['ijtimoiy-tarmoq'])
class SocialAccountRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SocialAccountSerializer
    permission_classes = [IsAuthenticated, ]
    #anu permission da yasagan codimni shotga chaqirdim! 
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = SocialNetwork.objects.all()
    lookup_field = 'pk'