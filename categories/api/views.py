from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly

class CategoryViewSet(ModelViewSet):
    #  permisos para la api
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    #  esto es lo que se va a mostrar en la api 
    queryset = Category.objects.all()
    # serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # lookup_field = 'slug'