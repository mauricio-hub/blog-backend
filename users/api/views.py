from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from rest_framework.permissions import IsAuthenticated
from users.api.serializers import UserRegisterSerilizer, UserSerializer


#esta vista crea un usuario
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerilizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#esta vista retorna todos los datos del usuario
# class UserView(APIView):
#     permission_classes = [ IsAuthenticated ]

#     def get(self,request):
#         # en request.user tenemos el usuario autenticado
#         serializer=UserSerializer(request.user)
#         serializer.data.pop('password')
#         return Response(serializer.data)
#esta vista retorna todos los datos del usuario
class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        data = serializer.data
        data.pop('password')  # Elimina el campo de contraseña de los datos
        return Response(data)   



