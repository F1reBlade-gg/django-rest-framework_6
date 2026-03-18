from rest_framework.permissions import BasePermission


class IsAuthenticatedOrCreateOnly(BasePermission):
    """
    Разрешает доступ только аутентифицированным пользователям для создания,
    но позволяет читать всем.
    """
    
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user and request.user.is_authenticated


class IsAuthenticatedOrReadOnly(BasePermission):
    """
    Разрешает доступ только аутентифицированным пользователям для изменения данных,
    но позволяет читать всем.
    """
    
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user and request.user.is_authenticated


class IsManagerOrReadOnly(BasePermission):
    """
    Разрешает доступ только менеджерам для изменения данных,
    но позволяет читать всем.
    """
    
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user and request.user.is_authenticated and request.user.is_manager
