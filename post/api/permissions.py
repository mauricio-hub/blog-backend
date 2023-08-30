from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # si es un usuario anonimo solo puede ver los post
        if request.method in ['GET']:
            return True
        else:
            # si es un usuario autenticado puede crear post
            # si es un usuario admin puede crear, editar y eliminar post
            return request.user.is_staff
        