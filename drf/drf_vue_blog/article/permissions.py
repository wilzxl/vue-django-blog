from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Only admin can modify
    Users can only view
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser
