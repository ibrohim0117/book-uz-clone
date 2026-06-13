from django.contrib import admin
from .models import Users, SocialNetwork



@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']
    search_fields = ['title', ]


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'full_name', 'phone', 'role', 'is_active', 'id']
    search_fields = ['username', 'first_name', 'phone']
    list_editable = ['role', 'is_active']
