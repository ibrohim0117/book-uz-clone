from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes


from rest_framework.generics import (
    CreateAPIView, RetrieveUpdateDestroyAPIView,
    RetrieveAPIView, RetrieveUpdateAPIView
)

from .serializers import UserRegisterSerializer, UserProfileSerializer, SocialAccountSerializer, UserCartSerializer
from .models import Users, SocialNetwork



@extend_schema(tags=['Register'])
class RegisterCreateAPIView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserRegisterSerializer

    

    
@extend_schema(tags=['User/Profile'])
class ProfileRetrieveAPIView(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    


@extend_schema(tags=['social_account-create'])
class SocialAccountCreateAPIView(CreateAPIView):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialAccountSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)



@extend_schema(
    tags=['social_account-update'],
    # Swagger-ga so'rovda 'title' degan parametr kelishini majburiy qilib ko'rsatamiz:
    parameters=[
        OpenApiParameter(
            name='title', 
            type=OpenApiTypes.STR, 
            location=OpenApiParameter.QUERY, # URL oxirida ?title=telegram bo'lib kelishi uchun
            required=True, 
            description="O'zgartirmoqchi yoki o'chirmoqchi bo'lgan ijtimoiy tarmoq nomi (masalan: telegram)"
        ),
    ]
)
class SocialAccountRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SocialAccountSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        title = self.request.data.get('title') or self.request.query_params.get('title')
        
        if not title:
            raise ValidationError(
                {"title": "Ijtimoiy tarmoqni yangilash yoki o'chirish uchun 'title' (nomi) yuborilishi shart!"}
            )
            
        try:
            return SocialNetwork.objects.get(user=self.request.user, title=title)
        except SocialNetwork.DoesNotExist:
            raise NotFound(f"Sizning hisobingizda '{title}' nomli ijtimoiy tarmoq topilmadi.")

    
