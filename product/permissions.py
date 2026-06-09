from rest_framework.permissions import BasePermission
from users.models import Users


class IsAdminRoleUser(BasePermission):
    """
    Allows access only to admin role users.
    """

    def has_permission(self, request, view):
        if request.user and request.user.role == Users.RoleChoices.ADMIN:
            return True
        return False
