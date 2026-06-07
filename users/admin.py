from django.contrib import admin
from .models import Users, SocialNetwork



@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']
    search_fields = ['title', ]



admin.site.register(Users)

