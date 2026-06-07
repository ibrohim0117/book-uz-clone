from rest_framework.permissions import BasePermission
from users.models import Users


class IsAdminRoleUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        if request.user and request.user.role == Users.RoleChoices.ADMIN:
            return True
        return False
        # return bool(request.user and request.user.role.admin)