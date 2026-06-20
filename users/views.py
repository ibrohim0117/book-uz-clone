from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes


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

from .models import Users, SocialNetwork, Cart
from .permissions import IsOwner
from .pagination import SocialAccountPagination, CartPagination



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
    serializer_class = SocialAccountSerializer
    permission_classes = [IsAuthenticated, ]
    pagination_class = SocialAccountPagination

    def get_queryset(self):
        # foydalanuvchi faqat o'zining social akkauntlarini ko'radi
        return SocialNetwork.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)



@extend_schema(request=SocialAccountSerializer, tags=['ijtimoiy-tarmoq'])
class SocialAccountRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SocialAccountSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = SocialNetwork.objects.all()
    lookup_field = 'pk'
    # IsOwner permission has_object_permission orqali faqat o'ziga tegishli
    # bo'lgan id'ni o'zgartirish/o'chirish mumkinligini tekshiradi - TODO item 7



@extend_schema(tags=['cart'])
class CartListCreateAPIView(ListCreateAPIView):
    serializer_class = UserCartSerializer
    permission_classes = [IsAuthenticated, ]
    pagination_class = CartPagination

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)



@extend_schema(tags=['cart'])
class CartRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserCartSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    lookup_field = 'pk'

    def get_queryset(self):
        # IsOwner bilan birgalikda ikki bosqichli himoya - TODO item 7,8
        return Cart.objects.filter(user=self.request.user)


