from django.contrib.auth.models import Group
from rest_framework import permissions


def _is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None


class IsUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        self.has_permission(request, view)

    def has_permission(self, request, view):
        has_group_permission = _is_in_group(request.user, 'user')
        return request.user and has_group_permission


class IsStaff(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        self.has_permission(request, view)

    def has_permission(self, request, view):
        has_group_permission = _is_in_group(request.user, 'staff')
        return request.user and has_group_permission


class IsCook(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        self.has_permission(request, view)

    def has_permission(self, request, view):
        has_group_permission = _is_in_group(request.user, 'cook')
        return request.user and has_group_permission


class IsAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        self.has_permission(request, view)

    def has_permission(self, request, view):
        has_group_permission = _is_in_group(request.user, 'admin')
        return request.user and has_group_permission
