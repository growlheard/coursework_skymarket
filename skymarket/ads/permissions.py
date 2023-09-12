from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsAdminOrAuthorOrReadOnly(permissions.BasePermission):
    """
    Проверка разрешений для доступа к объекту модели.

    Разрешает доступ только для чтения (SAFE_METHODS) или если пользователь является администратором или автором объекта.
    """

    def has_object_permission(self, request, view, obj):
        """
        Проверяет, имеет ли пользователь разрешение на доступ к объекту.

        Разрешает доступ, если метод запроса является безопасным (SAFE_METHODS),
        или если пользователь является администратором,
        или если пользователь является автором объекта.
        """
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        return obj.author == request.user

    def has_permission(self, request, view):
        """
        Проверяет, имеет ли пользователь разрешение на выполнение операции.

        Разрешает доступ, если метод запроса является безопасным (SAFE_METHODS),
        или если пользователь аутентифицирован.
        """
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated


class IsReadOnlyOrAuthenticated(permissions.BasePermission):
    """
    Проверка разрешений для доступа к объекту модели.

    Разрешает доступ только для чтения (SAFE_METHODS) или если пользователь аутентифицирован.
    """

    def has_permission(self, request, view):
        """
        Проверяет, имеет ли пользователь разрешение на выполнение операции.

        Разрешает доступ, если метод запроса является безопасным (SAFE_METHODS),
        или если пользователь аутентифицирован.
        """
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated
