from rest_framework.permissions import BasePermission
from comments.models import Comment

class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # si la peticion es GET o POST, se permite ver  o crear un comentario
        if request.method in 'GET' or request.method in 'POST':
            return True
        else:
            #sacamos el id del comentario que queremos editar o eliminar
            id_comment = view.kwargs['pk']
            # traemos el comentario que queremos editar o eliminar
            comment = Comment.objects.get(pk=id_comment)
            # sacamos el id del usuario que hizo la peticion
            id_user = request.user.pk
            # sacamos el id del usuario que hizo el comentario
            id_user_comment = comment.user_id

            # si el usuario que hizo la peticion es el mismo que hizo el comentario 
            # se permite editar o eliminar el comentario  
            if id_user == id_user_comment:
                return True
            
            return False
