from rest_framework.permissions import BasePermission

class IsAdminRoleUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)
from users.models import Users


class IsAdminRoleUser(BasePermission):
    """
    Allows access only to admin role users.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == Users.RoleChoices.ADMIN:
            return True
        return False
