from rest_framework import permissions


class isOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission only to only allow owners of an object to edit it
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user