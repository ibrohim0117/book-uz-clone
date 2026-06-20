from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Foydalanuvchi faqat o'ziga tegishli object (SocialNetwork, Cart va h.k.)ni
    o'zgartirishi yoki o'chirishi mumkin - TODO item 7.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user.id
