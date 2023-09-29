from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from rest_framework.permissions import IsAuthenticated
from users.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from users.models import User

#esta vista crea un usuario
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#esta vista retorna todos los datos del usuario
class UserView(APIView):
    permission_classes = [ IsAuthenticated ]

    def get(self,request):
        # en request.user tenemos el usuario autenticado
        serializer=UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


